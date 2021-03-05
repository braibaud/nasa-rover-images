import os
import io_common as ic
import rover as ro
import rss_curiosity as rc


class CuriosityConfig(ro.RoverConfigBase):

    def get_empty_database(self):
        return rc.ItemList([])

    async def process_feed(self, incremental):
        page = 0

        total_images = {
            'valid': 0,
            'added': 0,
            'total': 0
        }

        while True:
            page_images = {
                'valid': 0,
                'added': 0,
                'total': 0
            }

            feed = await rc.get_feed_images(
                url=rc.get_feed_page(
                    page=page))

            if feed is None:
                print('STOP: no feed')
                break

            if feed.items is None:
                print('STOP: no images')
                break

            nb_images = len(feed.items)

            if nb_images == 0:
                print('stSTOPop: empty image list')
                break

            page_images['total'] += nb_images

            for image in feed.items:
                await self.process_image(
                    page_images=page_images,
                    image=image)

            print('page {0}: {1} added, {2} valid, {3} total'.format(
                page,
                page_images['added'],
                page_images['valid'],
                page_images['total']))

            total_images['added'] += page_images['added']
            total_images['valid'] += page_images['valid']
            total_images['total'] += page_images['total']

            if incremental and page_images['added'] == 0:
                print('STOP: no more updates')
                break

            page += 1

        print('TOTAL: {0} pages, {1} added, {2} valid, {3} total'.format(
            page - 1,
            total_images['added'],
            total_images['valid'],
            total_images['total']))

    async def process_image(self, page_images, image):

        image_file_path = os.path.join(
            self.folder,
            '{0}.png'.format(image.imageid))

        valid_image = False

        if not image.is_thumbnail or self.thumbnail:
            valid_image = True

        if valid_image:
            page_images['valid'] += 1

            if not rc.exists(
                self.database.items,
                image.imageid):

                self.database.items.append(image)
                page_images['added'] += 1

            if not os.path.exists(image_file_path):
                await ic.get_image(
                    image.url
                    ,
                    image_file_path)
