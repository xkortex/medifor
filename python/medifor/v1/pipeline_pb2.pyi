# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from medifor.v1.analytic_pb2 import (
    Detection as medifor___v1___analytic_pb2___Detection,
)

from medifor.v1.fusion_pb2 import (
    Fusion as medifor___v1___fusion_pb2___Fusion,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class DetectionStage(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> DetectionStage: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[DetectionStage]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, DetectionStage]]: ...
    DETECTION_STAGE_NONE = typing___cast(DetectionStage, 0)
    DETECTION_STAGE_QUEUED = typing___cast(DetectionStage, 1)
    DETECTION_STAGE_CLAIMED = typing___cast(DetectionStage, 2)
    DETECTION_STAGE_FINISHED = typing___cast(DetectionStage, 3)
DETECTION_STAGE_NONE = typing___cast(DetectionStage, 0)
DETECTION_STAGE_QUEUED = typing___cast(DetectionStage, 1)
DETECTION_STAGE_CLAIMED = typing___cast(DetectionStage, 2)
DETECTION_STAGE_FINISHED = typing___cast(DetectionStage, 3)

class DetectionStatus(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> DetectionStatus: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[DetectionStatus]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, DetectionStatus]]: ...
    DETECTION_STATUS_NONE = typing___cast(DetectionStatus, 0)
    DETECTION_STATUS_SUCCESS = typing___cast(DetectionStatus, 1)
    DETECTION_STATUS_FAILURE = typing___cast(DetectionStatus, 2)
DETECTION_STATUS_NONE = typing___cast(DetectionStatus, 0)
DETECTION_STATUS_SUCCESS = typing___cast(DetectionStatus, 1)
DETECTION_STATUS_FAILURE = typing___cast(DetectionStatus, 2)

class SortKey(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> SortKey: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[SortKey]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, SortKey]]: ...
    SCORE = typing___cast(SortKey, 0)
    META = typing___cast(SortKey, 1)
SCORE = typing___cast(SortKey, 0)
META = typing___cast(SortKey, 1)

class FusionThresholdType(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> FusionThresholdType: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[FusionThresholdType]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, FusionThresholdType]]: ...
    FUSION_NO_THRESHOLD = typing___cast(FusionThresholdType, 0)
    FUSION_LT_THRESHOLD = typing___cast(FusionThresholdType, 1)
    FUSION_GT_THRESHOLD = typing___cast(FusionThresholdType, 2)
FUSION_NO_THRESHOLD = typing___cast(FusionThresholdType, 0)
FUSION_LT_THRESHOLD = typing___cast(FusionThresholdType, 1)
FUSION_GT_THRESHOLD = typing___cast(FusionThresholdType, 2)

class SortCol(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    key = ... # type: SortKey
    is_asc = ... # type: bool
    type_cast = ... # type: typing___Text
    meta_key = ... # type: typing___Text

    def __init__(self,
        *,
        key : typing___Optional[SortKey] = None,
        is_asc : typing___Optional[bool] = None,
        type_cast : typing___Optional[typing___Text] = None,
        meta_key : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SortCol: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"is_asc",u"key",u"meta_key",u"type_cast"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"is_asc",b"is_asc",u"key",b"key",u"meta_key",b"meta_key",u"type_cast",b"type_cast"]) -> None: ...

class DetectionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DetectionRequest.TagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class UserTagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DetectionRequest.UserTagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class MetaEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DetectionRequest.MetaEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    id = ... # type: typing___Text
    analytic_id = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    fuser_id = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    analytic_timeout_sec = ... # type: int

    @property
    def request(self) -> medifor___v1___analytic_pb2___Detection: ...

    @property
    def tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    @property
    def user_tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    @property
    def meta(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        request : typing___Optional[medifor___v1___analytic_pb2___Detection] = None,
        analytic_id : typing___Optional[typing___Iterable[typing___Text]] = None,
        fuser_id : typing___Optional[typing___Iterable[typing___Text]] = None,
        tags : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        user_tags : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        meta : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        analytic_timeout_sec : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DetectionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"request"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"analytic_id",u"analytic_timeout_sec",u"fuser_id",u"id",u"meta",u"request",u"tags",u"user_tags"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"request",b"request"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"analytic_id",b"analytic_id",u"analytic_timeout_sec",b"analytic_timeout_sec",u"fuser_id",b"fuser_id",u"id",b"id",u"meta",b"meta",u"request",b"request",u"tags",b"tags",u"user_tags",b"user_tags"]) -> None: ...

class AnalyticDetectionInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    analytic_id = ... # type: typing___Text
    stage = ... # type: DetectionStage
    status = ... # type: DetectionStatus

    @property
    def detection(self) -> medifor___v1___analytic_pb2___Detection: ...

    def __init__(self,
        *,
        analytic_id : typing___Optional[typing___Text] = None,
        stage : typing___Optional[DetectionStage] = None,
        status : typing___Optional[DetectionStatus] = None,
        detection : typing___Optional[medifor___v1___analytic_pb2___Detection] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AnalyticDetectionInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"detection"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"analytic_id",u"detection",u"stage",u"status"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"detection",b"detection"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"analytic_id",b"analytic_id",u"detection",b"detection",u"stage",b"stage",u"status",b"status"]) -> None: ...

class DetectionInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DetectionInfo.TagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class UserTagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DetectionInfo.UserTagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class MetaEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DetectionInfo.MetaEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    id = ... # type: typing___Text
    has_fused = ... # type: bool
    fused_score = ... # type: float
    analytics_total = ... # type: int
    analytics_finished = ... # type: int

    @property
    def analytic_info(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AnalyticDetectionInfo]: ...

    @property
    def fusion_info(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FuserFusionInfo]: ...

    @property
    def tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    @property
    def user_tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    @property
    def meta(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        analytic_info : typing___Optional[typing___Iterable[AnalyticDetectionInfo]] = None,
        fusion_info : typing___Optional[typing___Iterable[FuserFusionInfo]] = None,
        tags : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        user_tags : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        meta : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        has_fused : typing___Optional[bool] = None,
        fused_score : typing___Optional[float] = None,
        analytics_total : typing___Optional[int] = None,
        analytics_finished : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DetectionInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"analytic_info",u"analytics_finished",u"analytics_total",u"fused_score",u"fusion_info",u"has_fused",u"id",u"meta",u"tags",u"user_tags"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"analytic_info",b"analytic_info",u"analytics_finished",b"analytics_finished",u"analytics_total",b"analytics_total",u"fused_score",b"fused_score",u"fusion_info",b"fusion_info",u"has_fused",b"has_fused",u"id",b"id",u"meta",b"meta",u"tags",b"tags",u"user_tags",b"user_tags"]) -> None: ...

class DetectionInfoRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    want_fused = ... # type: bool

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        want_fused : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DetectionInfoRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id",u"want_fused"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"want_fused",b"want_fused"]) -> None: ...

class DetectionListRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DetectionListRequest.TagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    detection_ids = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    want_fused = ... # type: bool
    fuser_id = ... # type: typing___Text
    fusion_threshold_type = ... # type: FusionThresholdType
    fusion_threshold_value = ... # type: float
    page_size = ... # type: int
    page_token = ... # type: typing___Text

    @property
    def tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    @property
    def order_by(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[SortCol]: ...

    def __init__(self,
        *,
        tags : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        detection_ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        want_fused : typing___Optional[bool] = None,
        order_by : typing___Optional[typing___Iterable[SortCol]] = None,
        fuser_id : typing___Optional[typing___Text] = None,
        fusion_threshold_type : typing___Optional[FusionThresholdType] = None,
        fusion_threshold_value : typing___Optional[float] = None,
        page_size : typing___Optional[int] = None,
        page_token : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DetectionListRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"detection_ids",u"fuser_id",u"fusion_threshold_type",u"fusion_threshold_value",u"order_by",u"page_size",u"page_token",u"tags",u"want_fused"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"detection_ids",b"detection_ids",u"fuser_id",b"fuser_id",u"fusion_threshold_type",b"fusion_threshold_type",u"fusion_threshold_value",b"fusion_threshold_value",u"order_by",b"order_by",u"page_size",b"page_size",u"page_token",b"page_token",u"tags",b"tags",u"want_fused",b"want_fused"]) -> None: ...

class DetectionList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    total = ... # type: int
    page_token = ... # type: typing___Text

    @property
    def detections(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DetectionInfo]: ...

    def __init__(self,
        *,
        detections : typing___Optional[typing___Iterable[DetectionInfo]] = None,
        total : typing___Optional[int] = None,
        page_token : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DetectionList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"detections",u"page_token",u"total"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"detections",b"detections",u"page_token",b"page_token",u"total",b"total"]) -> None: ...

class FusionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> FusionRequest.TagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    id = ... # type: typing___Text
    fuser_id = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    detection_id = ... # type: typing___Text
    detection_id_out_dir = ... # type: typing___Text

    @property
    def request(self) -> medifor___v1___fusion_pb2___Fusion: ...

    @property
    def tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        request : typing___Optional[medifor___v1___fusion_pb2___Fusion] = None,
        fuser_id : typing___Optional[typing___Iterable[typing___Text]] = None,
        tags : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        detection_id : typing___Optional[typing___Text] = None,
        detection_id_out_dir : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FusionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"request"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"detection_id",u"detection_id_out_dir",u"fuser_id",u"id",u"request",u"tags"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"request",b"request"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"detection_id",b"detection_id",u"detection_id_out_dir",b"detection_id_out_dir",u"fuser_id",b"fuser_id",u"id",b"id",u"request",b"request",u"tags",b"tags"]) -> None: ...

class FuserFusionInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    fuser_id = ... # type: typing___Text
    stage = ... # type: DetectionStage
    status = ... # type: DetectionStatus

    @property
    def fusion(self) -> medifor___v1___fusion_pb2___Fusion: ...

    def __init__(self,
        *,
        fuser_id : typing___Optional[typing___Text] = None,
        stage : typing___Optional[DetectionStage] = None,
        status : typing___Optional[DetectionStatus] = None,
        fusion : typing___Optional[medifor___v1___fusion_pb2___Fusion] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FuserFusionInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"fusion"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"fuser_id",u"fusion",u"stage",u"status"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"fusion",b"fusion"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"fuser_id",b"fuser_id",u"fusion",b"fusion",u"stage",b"stage",u"status",b"status"]) -> None: ...

class FusionInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> FusionInfo.TagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    id = ... # type: typing___Text
    has_fused = ... # type: bool
    fused_score = ... # type: float

    @property
    def fusion_infos(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FuserFusionInfo]: ...

    @property
    def tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        fusion_infos : typing___Optional[typing___Iterable[FuserFusionInfo]] = None,
        tags : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        has_fused : typing___Optional[bool] = None,
        fused_score : typing___Optional[float] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FusionInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"fused_score",u"fusion_infos",u"has_fused",u"id",u"tags"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"fused_score",b"fused_score",u"fusion_infos",b"fusion_infos",u"has_fused",b"has_fused",u"id",b"id",u"tags",b"tags"]) -> None: ...

class FuseAllIDsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    fuser_id = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    out_dir = ... # type: typing___Text

    def __init__(self,
        *,
        fuser_id : typing___Optional[typing___Iterable[typing___Text]] = None,
        out_dir : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FuseAllIDsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"fuser_id",u"out_dir"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"fuser_id",b"fuser_id",u"out_dir",b"out_dir"]) -> None: ...

class FuseAllIDsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FuseAllIDsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class UpdateDetectionTagsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> UpdateDetectionTagsRequest.TagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    detection_id = ... # type: typing___Text
    replace = ... # type: bool
    delete_tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        detection_id : typing___Optional[typing___Text] = None,
        replace : typing___Optional[bool] = None,
        tags : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        delete_tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdateDetectionTagsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"delete_tags",u"detection_id",u"replace",u"tags"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"delete_tags",b"delete_tags",u"detection_id",b"detection_id",u"replace",b"replace",u"tags",b"tags"]) -> None: ...

class DetectionTagInfoRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DetectionTagInfoRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class DetectionTagInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagCountsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: int

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[int] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DetectionTagInfo.TagCountsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class UserTagCountsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: int

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[int] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DetectionTagInfo.UserTagCountsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


    @property
    def tag_counts(self) -> typing___MutableMapping[typing___Text, int]: ...

    @property
    def user_tag_counts(self) -> typing___MutableMapping[typing___Text, int]: ...

    def __init__(self,
        *,
        tag_counts : typing___Optional[typing___Mapping[typing___Text, int]] = None,
        user_tag_counts : typing___Optional[typing___Mapping[typing___Text, int]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DetectionTagInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"tag_counts",u"user_tag_counts"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"tag_counts",b"tag_counts",u"user_tag_counts",b"user_tag_counts"]) -> None: ...

class DeleteDetectionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    detection_id = ... # type: typing___Text

    def __init__(self,
        *,
        detection_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeleteDetectionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"detection_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"detection_id",b"detection_id"]) -> None: ...

class Empty(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Empty: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
