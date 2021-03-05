from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser
import aiohttp
import io_common as ic


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Extended:
    lmst: Optional[str] = None
    bucket: Optional[str] = None
    mast_az: Optional[str] = None
    mast_el: Optional[str] = None
    url_list: Optional[str] = None
    contributor: Optional[str] = None
    filter_name: Optional[str] = None
    sample_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Extended':
        assert isinstance(obj, dict)
        lmst = from_union([from_none, from_str], obj.get("lmst"))
        bucket = from_union([from_str, from_none], obj.get("bucket"))
        mast_az = from_union([from_none, from_str], obj.get("mast_az"))
        mast_el = from_union([from_none, from_str], obj.get("mast_el"))
        url_list = from_union([from_str, from_none], obj.get("url_list"))
        contributor = from_union([from_str, from_none], obj.get("contributor"))
        filter_name = from_union([from_none, from_str], obj.get("filter_name"))
        sample_type = from_union([from_str, from_none], obj.get("sample_type"))
        return Extended(lmst, bucket, mast_az, mast_el, url_list, contributor, filter_name, sample_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lmst"] = from_union([from_none, from_str], self.lmst)
        result["bucket"] = from_union([from_str, from_none], self.bucket)
        result["mast_az"] = from_union([from_none, from_str], self.mast_az)
        result["mast_el"] = from_union([from_none, from_str], self.mast_el)
        result["url_list"] = from_union([from_str, from_none], self.url_list)
        result["contributor"] = from_union(
            [from_str, from_none], self.contributor)
        result["filter_name"] = from_union(
            [from_none, from_str], self.filter_name)
        result["sample_type"] = from_union(
            [from_str, from_none], self.sample_type)
        return result


@dataclass
class Item:
    id_: Optional[int] = None
    camera_vector: Optional[str] = None
    site: Optional[int] = None
    imageid: Optional[str] = None
    subframe_rect: Optional[str] = None
    sol: Optional[int] = None
    scale_factor: Optional[int] = None
    camera_model_component_list: Optional[str] = None
    instrument: Optional[str] = None
    url: Optional[str] = None
    spacecraft_clock: Optional[float] = None
    attitude: Optional[str] = None
    camera_position: Optional[str] = None
    camera_model_type: Optional[str] = None
    drive: Optional[int] = None
    xyz: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    mission: Optional[str] = None
    extended: Optional[Extended] = None
    date_taken: Optional[datetime] = None
    date_received: Optional[datetime] = None
    instrument_sort: Optional[int] = None
    sample_type_sort: Optional[int] = None
    is_thumbnail: Optional[bool] = None
    title: Optional[str] = None
    description: Optional[str] = None
    link: Optional[str] = None
    image_credit: Optional[str] = None
    https_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id_ = from_union([from_int, from_none], obj.get("id"))
        camera_vector = from_union(
            [from_none, from_str], obj.get("camera_vector"))
        site = from_union([from_int, from_none], obj.get("site"))
        imageid = from_union([from_str, from_none], obj.get("imageid"))
        subframe_rect = from_union(
            [from_none, from_str], obj.get("subframe_rect"))
        sol = from_union([from_int, from_none], obj.get("sol"))
        scale_factor = from_union(
            [from_int, from_none], obj.get("scale_factor"))
        camera_model_component_list = from_union(
            [from_none, from_str], obj.get("camera_model_component_list"))
        instrument = from_union([from_str, from_none], obj.get("instrument"))
        url = from_union([from_str, from_none], obj.get("url"))
        spacecraft_clock = from_union(
            [from_none, from_float], obj.get("spacecraft_clock"))
        attitude = from_union([from_none, from_str], obj.get("attitude"))
        camera_position = from_union(
            [from_none, from_str], obj.get("camera_position"))
        camera_model_type = from_union(
            [from_none, from_str], obj.get("camera_model_type"))
        drive = from_union([from_int, from_none], obj.get("drive"))
        xyz = from_union([from_none, from_str], obj.get("xyz"))
        created_at = from_union(
            [from_datetime, from_none], obj.get("created_at"))
        updated_at = from_union(
            [from_datetime, from_none], obj.get("updated_at"))
        mission = from_union([from_str, from_none], obj.get("mission"))
        extended = from_union(
            [Extended.from_dict, from_none], obj.get("extended"))
        date_taken = from_union(
            [from_datetime, from_none], obj.get("date_taken"))
        date_received = from_union(
            [from_datetime, from_none], obj.get("date_received"))
        instrument_sort = from_union(
            [from_int, from_none], obj.get("instrument_sort"))
        sample_type_sort = from_union(
            [from_int, from_none], obj.get("sample_type_sort"))
        is_thumbnail = from_union(
            [from_bool, from_none], obj.get("is_thumbnail"))
        title = from_union([from_str, from_none], obj.get("title"))
        description = from_union([from_str, from_none], obj.get("description"))
        link = from_union([from_str, from_none], obj.get("link"))
        image_credit = from_union(
            [from_str, from_none], obj.get("image_credit"))
        https_url = from_union([from_str, from_none], obj.get("https_url"))
        return Item(id_, camera_vector, site, imageid, subframe_rect, sol, scale_factor, camera_model_component_list, instrument, url, spacecraft_clock, attitude, camera_position, camera_model_type, drive, xyz, created_at, updated_at, mission, extended, date_taken, date_received, instrument_sort, sample_type_sort, is_thumbnail, title, description, link, image_credit, https_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id_)
        result["camera_vector"] = from_union(
            [from_none, from_str], self.camera_vector)
        result["site"] = from_union([from_int, from_none], self.site)
        result["imageid"] = from_union([from_str, from_none], self.imageid)
        result["subframe_rect"] = from_union(
            [from_none, from_str], self.subframe_rect)
        result["sol"] = from_union([from_int, from_none], self.sol)
        result["scale_factor"] = from_union(
            [from_int, from_none], self.scale_factor)
        result["camera_model_component_list"] = from_union(
            [from_none, from_str], self.camera_model_component_list)
        result["instrument"] = from_union(
            [from_str, from_none], self.instrument)
        result["url"] = from_union([from_str, from_none], self.url)
        result["spacecraft_clock"] = from_union(
            [from_none, to_float], self.spacecraft_clock)
        result["attitude"] = from_union([from_none, from_str], self.attitude)
        result["camera_position"] = from_union(
            [from_none, from_str], self.camera_position)
        result["camera_model_type"] = from_union(
            [from_none, from_str], self.camera_model_type)
        result["drive"] = from_union([from_int, from_none], self.drive)
        result["xyz"] = from_union([from_none, from_str], self.xyz)
        result["created_at"] = from_union(
            [lambda x: x.isoformat(), from_none], self.created_at)
        result["updated_at"] = from_union(
            [lambda x: x.isoformat(), from_none], self.updated_at)
        result["mission"] = from_union([from_str, from_none], self.mission)
        result["extended"] = from_union(
            [lambda x: to_class(Extended, x), from_none], self.extended)
        result["date_taken"] = from_union(
            [lambda x: x.isoformat(), from_none], self.date_taken)
        result["date_received"] = from_union(
            [lambda x: x.isoformat(), from_none], self.date_received)
        result["instrument_sort"] = from_union(
            [from_int, from_none], self.instrument_sort)
        result["sample_type_sort"] = from_union(
            [from_int, from_none], self.sample_type_sort)
        result["is_thumbnail"] = from_union(
            [from_bool, from_none], self.is_thumbnail)
        result["title"] = from_union([from_str, from_none], self.title)
        result["description"] = from_union(
            [from_str, from_none], self.description)
        result["link"] = from_union([from_str, from_none], self.link)
        result["image_credit"] = from_union(
            [from_str, from_none], self.image_credit)
        result["https_url"] = from_union([from_str, from_none], self.https_url)
        return result


@dataclass
class Feed:
    items: Optional[List[Item]] = None
    more: Optional[bool] = None
    total: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Feed':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_list(
            Item.from_dict, x), from_none], obj.get("items"))
        more = from_union([from_bool, from_none], obj.get("more"))
        total = from_union([from_int, from_none], obj.get("total"))
        page = from_union([from_int, from_none], obj.get("page"))
        per_page = from_union([from_int, from_none], obj.get("per_page"))
        return Feed(items, more, total, page, per_page)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_union([lambda x: from_list(
            lambda x: to_class(Item, x), x), from_none], self.items)
        result["more"] = from_union([from_bool, from_none], self.more)
        result["total"] = from_union([from_int, from_none], self.total)
        result["page"] = from_union([from_int, from_none], self.page)
        result["per_page"] = from_union([from_int, from_none], self.per_page)
        return result


@dataclass
class ItemList:
    items: Optional[List[Item]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemList':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_list(
            Item.from_dict, x), from_none], obj.get("items"))
        return ItemList(items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_union([lambda x: from_list(
            lambda x: to_class(Item, x), x), from_none], self.items)
        return result


def feed_from_dict(s: Any) -> Feed:
    return Feed.from_dict(s)


def feed_to_dict(x: Feed) -> Any:
    return to_class(Feed, x)


def itemlist_from_dict(s: Any) -> ItemList:
    return ItemList.from_dict(s)


def itemlist_to_dict(x: ItemList) -> Any:
    return to_class(ItemList, x)


def load_itemlist_from_json(file_path):
    return itemlist_from_dict(
        s=ic.load_json(
            file_path=file_path))


def save_itemlist_to_json(file_path, data):
    return ic.save_json(
        file_path=file_path,
        data=itemlist_to_dict(
            x=data))


def get_feed_page(page):
    url = 'https://mars.nasa.gov/api/v1/raw_image_items/?'
    url = url + 'order=sol+desc%2Cinstrument_sort+asc%2Csample_type_sort+asc%2C+date_taken+desc&'
    url = url + 'per_page=100&'
    url = url + 'page={0}&'.format(page)
    url = url + 'condition_1=msl%3Amission&'
    url = url + 'extended=thumbnail%3A%3Asample_type%3A%3Anoteq'
    return url


def exists(itemlist, imageid):
    for image in itemlist:
        if image.imageid == imageid:
            return True
    return False


async def get_feed_images(url):
    async with aiohttp.ClientSession() as session:
        return Feed.from_dict(await ic.fetch_json(session, url))
