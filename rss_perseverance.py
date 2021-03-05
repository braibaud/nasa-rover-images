from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser
import aiohttp
import io_common as ic


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Camera:
    filter_name: Optional[str] = None
    camera_vector: Optional[str] = None
    camera_model_component_list: Optional[str] = None
    camera_position: Optional[str] = None
    instrument: Optional[str] = None
    camera_model_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Camera':
        assert isinstance(obj, dict)
        filter_name = from_union([from_str, from_none], obj.get("filter_name"))
        camera_vector = from_union(
            [from_str, from_none], obj.get("camera_vector"))
        camera_model_component_list = from_union(
            [from_str, from_none], obj.get("camera_model_component_list"))
        camera_position = from_union(
            [from_str, from_none], obj.get("camera_position"))
        instrument = from_union([from_str, from_none], obj.get("instrument"))
        camera_model_type = from_union(
            [from_str, from_none], obj.get("camera_model_type"))
        return Camera(filter_name, camera_vector, camera_model_component_list, camera_position, instrument, camera_model_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["filter_name"] = from_union(
            [from_str, from_none], self.filter_name)
        result["camera_vector"] = from_union(
            [from_str, from_none], self.camera_vector)
        result["camera_model_component_list"] = from_union(
            [from_str, from_none], self.camera_model_component_list)
        result["camera_position"] = from_union(
            [from_str, from_none], self.camera_position)
        result["instrument"] = from_union(
            [from_str, from_none], self.instrument)
        result["camera_model_type"] = from_union(
            [from_str, from_none], self.camera_model_type)
        return result


@dataclass
class Extended:
    mast_az: Optional[str] = None
    mast_el: Optional[str] = None
    sclk: Optional[str] = None
    scale_factor: Optional[str] = None
    xyz: Optional[str] = None
    subframe_rect: Optional[str] = None
    dimension: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Extended':
        assert isinstance(obj, dict)
        mast_az = from_union([from_str, from_none], obj.get("mastAz"))
        mast_el = from_union([from_str, from_none], obj.get("mastEl"))
        sclk = from_union([from_str, from_none], obj.get("sclk"))
        scale_factor = from_union(
            [from_str, from_none], obj.get("scaleFactor"))
        xyz = from_union([from_str, from_none], obj.get("xyz"))
        subframe_rect = from_union(
            [from_str, from_none], obj.get("subframeRect"))
        dimension = from_union([from_str, from_none], obj.get("dimension"))
        return Extended(mast_az, mast_el, sclk, scale_factor, xyz, subframe_rect, dimension)

    def to_dict(self) -> dict:
        result: dict = {}
        result["mastAz"] = from_union([from_str, from_none], self.mast_az)
        result["mastEl"] = from_union([from_str, from_none], self.mast_el)
        result["sclk"] = from_union([from_str, from_none], self.sclk)
        result["scaleFactor"] = from_union(
            [from_str, from_none], self.scale_factor)
        result["xyz"] = from_union([from_str, from_none], self.xyz)
        result["subframeRect"] = from_union(
            [from_str, from_none], self.subframe_rect)
        result["dimension"] = from_union([from_str, from_none], self.dimension)
        return result


@dataclass
class ImageFiles:
    medium: Optional[str] = None
    small: Optional[str] = None
    full_res: Optional[str] = None
    large: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ImageFiles':
        assert isinstance(obj, dict)
        medium = from_union([from_str, from_none], obj.get("medium"))
        small = from_union([from_str, from_none], obj.get("small"))
        full_res = from_union([from_str, from_none], obj.get("full_res"))
        large = from_union([from_str, from_none], obj.get("large"))
        return ImageFiles(medium, small, full_res, large)

    def to_dict(self) -> dict:
        result: dict = {}
        result["medium"] = from_union([from_str, from_none], self.medium)
        result["small"] = from_union([from_str, from_none], self.small)
        result["full_res"] = from_union([from_str, from_none], self.full_res)
        result["large"] = from_union([from_str, from_none], self.large)
        return result


@dataclass
class Image:
    extended: Optional[Extended] = None
    sol: Optional[int] = None
    attitude: Optional[str] = None
    image_files: Optional[ImageFiles] = None
    imageid: Optional[str] = None
    camera: Optional[Camera] = None
    caption: Optional[str] = None
    sample_type: Optional[str] = None
    date_taken_mars: Optional[str] = None
    credit: Optional[str] = None
    date_taken_utc: Optional[datetime] = None
    json_link: Optional[str] = None
    link: Optional[str] = None
    drive: Optional[str] = None
    title: Optional[str] = None
    site: Optional[int] = None
    date_received: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        extended = from_union(
            [Extended.from_dict, from_none], obj.get("extended"))
        sol = from_union([from_int, from_none], obj.get("sol"))
        attitude = from_union([from_str, from_none], obj.get("attitude"))
        image_files = from_union(
            [ImageFiles.from_dict, from_none], obj.get("image_files"))
        imageid = from_union([from_str, from_none], obj.get("imageid"))
        camera = from_union([Camera.from_dict, from_none], obj.get("camera"))
        caption = from_union([from_str, from_none], obj.get("caption"))
        sample_type = from_union([from_str, from_none], obj.get("sample_type"))
        date_taken_mars = from_union(
            [from_str, from_none], obj.get("date_taken_mars"))
        credit = from_union([from_str, from_none], obj.get("credit"))
        date_taken_utc = from_union(
            [from_datetime, from_none], obj.get("date_taken_utc"))
        json_link = from_union([from_str, from_none], obj.get("json_link"))
        link = from_union([from_str, from_none], obj.get("link"))
        drive = from_union([from_str, from_none], obj.get("drive"))
        title = from_union([from_str, from_none], obj.get("title"))
        site = from_union([from_int, from_none], obj.get("site"))
        date_received = from_union(
            [from_datetime, from_none], obj.get("date_received"))
        return Image(extended, sol, attitude, image_files, imageid, camera, caption, sample_type, date_taken_mars, credit, date_taken_utc, json_link, link, drive, title, site, date_received)

    def to_dict(self) -> dict:
        result: dict = {}
        result["extended"] = from_union(
            [lambda x: to_class(Extended, x), from_none], self.extended)
        result["sol"] = from_union([from_int, from_none], self.sol)
        result["attitude"] = from_union([from_str, from_none], self.attitude)
        result["image_files"] = from_union(
            [lambda x: to_class(ImageFiles, x), from_none], self.image_files)
        result["imageid"] = from_union([from_str, from_none], self.imageid)
        result["camera"] = from_union(
            [lambda x: to_class(Camera, x), from_none], self.camera)
        result["caption"] = from_union([from_str, from_none], self.caption)
        result["sample_type"] = from_union(
            [from_str, from_none], self.sample_type)
        result["date_taken_mars"] = from_union(
            [from_str, from_none], self.date_taken_mars)
        result["credit"] = from_union([from_str, from_none], self.credit)
        result["date_taken_utc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.date_taken_utc)
        result["json_link"] = from_union([from_str, from_none], self.json_link)
        result["link"] = from_union([from_str, from_none], self.link)
        result["drive"] = from_union([from_str, from_none], self.drive)
        result["title"] = from_union([from_str, from_none], self.title)
        result["site"] = from_union([from_int, from_none], self.site)
        result["date_received"] = from_union(
            [lambda x: x.isoformat(), from_none], self.date_received)
        return result


@dataclass
class Checkbox:
    value: Optional[str] = None
    label: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Checkbox':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        label = from_union([from_str, from_none], obj.get("label"))
        return Checkbox(value, label)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["label"] = from_union([from_str, from_none], self.label)
        return result


@dataclass
class Nav:
    checkboxes: Optional[List[Checkbox]] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Nav':
        assert isinstance(obj, dict)
        checkboxes = from_union([lambda x: from_list(
            Checkbox.from_dict, x), from_none], obj.get("checkboxes"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Nav(checkboxes, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["checkboxes"] = from_union([lambda x: from_list(
            lambda x: to_class(Checkbox, x), x), from_none], self.checkboxes)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Feed:
    nav: Optional[List[Nav]] = None
    images: Optional[List[Image]] = None
    per_page: Optional[str] = None
    total_results: Optional[int] = None
    type_: Optional[str] = None
    page: Optional[str] = None
    mission: Optional[str] = None
    total_images: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Feed':
        assert isinstance(obj, dict)
        nav = from_union([lambda x: from_list(
            Nav.from_dict, x), from_none], obj.get("nav"))
        images = from_union([lambda x: from_list(
            Image.from_dict, x), from_none], obj.get("images"))
        per_page = from_union([from_str, from_none], obj.get("per_page"))
        total_results = from_union(
            [from_int, from_none], obj.get("total_results"))
        type_ = from_union([from_str, from_none], obj.get("type"))
        page = from_union([from_str, from_int, from_none], obj.get("page"))
        mission = from_union([from_str, from_none], obj.get("mission"))
        total_images = from_union(
            [from_int, from_none], obj.get("total_images"))
        return Feed(nav, images, per_page, total_results, type_, page, mission, total_images)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nav"] = from_union([lambda x: from_list(
            lambda x: to_class(Nav, x), x), from_none], self.nav)
        result["images"] = from_union([lambda x: from_list(
            lambda x: to_class(Image, x), x), from_none], self.images)
        result["per_page"] = from_union([from_str, from_none], self.per_page)
        result["total_results"] = from_union(
            [from_int, from_none], self.total_results)
        result["type"] = from_union([from_str, from_none], self.type_)
        result["page"] = from_union([from_str, from_none], self.page)
        result["mission"] = from_union([from_str, from_none], self.mission)
        result["total_images"] = from_union(
            [from_int, from_none], self.total_images)
        return result


@dataclass
class ImageList:
    images: Optional[List[Image]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ImageList':
        assert isinstance(obj, dict)
        images = from_union([lambda x: from_list(
            Image.from_dict, x), from_none], obj.get("images"))
        return ImageList(images)

    def to_dict(self) -> dict:
        result: dict = {}
        result["images"] = from_union([lambda x: from_list(
            lambda x: to_class(Image, x), x), from_none], self.images)
        return result


def feed_from_dict(s: Any) -> Feed:
    return Feed.from_dict(s)


def feed_to_dict(x: Feed) -> Any:
    return to_class(Feed, x)


def imagelist_from_dict(s: Any) -> ImageList:
    return ImageList.from_dict(s)


def imagelist_to_dict(x: ImageList) -> Any:
    return to_class(ImageList, x)


def load_imagelist_from_json(file_path):
    return imagelist_from_dict(
        s=ic.load_json(
            file_path=file_path))


def save_imagelist_to_json(file_path, data):
    return ic.save_json(
        file_path=file_path,
        data=imagelist_to_dict(
            x=data))


def get_feed_page(page):
    url = 'https://mars.nasa.gov/rss/api/?'
    url = url + 'feed=raw_images&'
    url = url + 'category=mars2020&'
    url = url + 'feedtype=json&'
    url = url + 'num=100&'
    url = url + 'page={0}&'.format(page)
    url = url + 'order=sol+desc&'
    url = url + 'search=|sample_type::full|,,&'
    url = url + 'extended=sample_type::full,'
    return url


def exists(imagelist, imageid):
    for image in imagelist:
        if image.imageid == imageid:
            return True
    return False


async def get_feed_images(url):
    async with aiohttp.ClientSession() as session:
        return Feed.from_dict(await ic.fetch_json(session, url))
