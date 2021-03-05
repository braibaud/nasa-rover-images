import os
import io_common as ic

class RoverConfigBase:
    
    def __init__(self, args) -> None:

        # all arguments
        self.args = args
        
        # the name of the rover
        self.name = str(args.rover_name)

        # whether or not to get thumnails also
        self.thumbnail = args.thumbnail

        # the output folder
        self.folder = os.path.join(
            args.cache_location,
            self.name)

        # name of the .npz database
        self.npz_db = os.path.join(
            self.folder,
            'images_{0}.npz'.format(
                self.name))

        # the current database
        self.database = self.__open_database()

    def __open_database(self):
        if os.path.exists(self.npz_db):
            return ic.load_data(
                file_path=self.npz_db)
        else:
            return self.get_empty_database()

    def save_database(self):
        '''Dumps the current database to disk'''
        ic.save_data(
            file_path=self.npz_db,
            data=self.database)

    def get_empty_database(self):
        '''Base class abstract implementation'''
        pass

    async def process_feed(self, incremental):
        '''Base class abstract implementation'''
        pass

    async def process_image(self, page_images, image):
        '''Base class abstract implementation'''
        pass

    async def run(self, incremental):
        try:
            await self.process_feed(incremental)
        finally:
            self.save_database()