from typing import Union, Iterable
import datetime
import asf_search.search

def geo_search(
        absoluteOrbit: Iterable[Union[int, range]] = None,
        asfFrame: Iterable[Union[int, range]] = None,
        beamMode: Iterable[str] = None,
        collectionName: Iterable[str] = None,
        end: datetime = None,
        flightDirection: Iterable[str] = None,
        frame: Iterable[Union[int, range]] = None,
        instrument: Iterable[str] = None,
        intersectsWith: str = None,
        lookDirection: Iterable[str] = None,
        maxResults: int = None,
        platform: Iterable[str] = None,
        polarization: Iterable[str] = None,
        processingDate: datetime = None,
        processingLevel: Iterable[str] = None,
        relativeOrbit: Iterable[Union[int, range]] = None,
        start: datetime = None,
        host: str = asf_search.INTERNAL.HOST
) -> dict:
    """
    Performs a geographic search using the ASF SearchAPI

    :param absoluteOrbit: For ALOS, ERS-1, ERS-2, JERS-1, and RADARSAT-1, Sentinel-1A, Sentinel-1B this value corresponds to the orbit count within the orbit cycle. For UAVSAR it is the Flight ID.
    :param asfFrame: This is primarily an ASF / JAXA frame reference. However, some platforms use other conventions. See ‘frame’ for ESA-centric frame searches.
    :param beamMode: The beam mode used to acquire the data.
    :param collectionName: For UAVSAR and AIRSAR data collections only. Search by general location, site description, or data grouping as supplied by flight agency or project.
    :param end: End date of data acquisition. Supports timestamps as well as natural language such as "3 weeks ago"
    :param flightDirection: Satellite orbit direction during data acquisition
    :param frame: ESA-referenced frames are offered to give users a universal framing convention. Each ESA frame has a corresponding ASF frame assigned. See also: asfframe
    :param instrument: The instrument used to acquire the data. See also: platform
    :param intersectsWith: Search by polygon, linestring, or point defined in 2D Well-Known Text (WKT)
    :param lookDirection: Left or right look direction during data acquisition
    :param maxResults: The maximum number of results to be returned by the search
    :param platform: Remote sensing platform that acquired the data. Platforms that work together, such as Sentinel-1A/1B and ERS-1/2 have multi-platform aliases available. See also: instrument
    :param polarization: A property of SAR electromagnetic waves that can be used to extract meaningful information about surface properties of the earth.
    :param processingDate: Used to find data that has been processed at ASF since a given time and date
    :param processingLevel: Level to which the data has been processed
    :param relativeOrbit: Path or track of satellite during data acquisition. For UAVSAR it is the Line ID.
    :param start: Start date of data acquisition. Supports timestamps as well as natural language such as "3 weeks ago"
    :param host: SearchAPI host, defaults to Production SearchAPI. This option is intended for dev/test purposes.

    :return: Dictionary of search results. Always includes 'results', may also include 'errors' and/or 'warnings'
    """

    kwargs = locals()
    data = dict((k,v) for k,v in kwargs.items() if v is not None and v != '')

    return asf_search.search(**data)