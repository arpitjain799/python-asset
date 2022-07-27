# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.cloud.asset_v1.types import assets as gca_assets
from google.iam.v1 import policy_pb2  # type: ignore
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore
from google.type import expr_pb2  # type: ignore

__manifest__ = (
    "ExportAssetsRequest",
    "ListAssetsRequest",
    "BatchGetAssetsHistoryRequest",
    "CreateFeedRequest",
    "GetFeedRequest",
    "ListFeedsRequest",
    "UpdateFeedRequest",
    "DeleteFeedRequest",
    "SearchAllResourcesRequest",
    "SearchAllIamPoliciesRequest",
    "AnalyzeIamPolicyRequest",
    "AnalyzeIamPolicyLongrunningRequest",
    "CreateSavedQueryRequest",
    "GetSavedQueryRequest",
    "ListSavedQueriesRequest",
    "UpdateSavedQueryRequest",
    "DeleteSavedQueryRequest",
    "AnalyzeMoveRequest",
    "BatchGetEffectiveIamPoliciesRequest",
)


class ExportAssetsRequest(proto.Message):
    r"""Export asset request.

    Attributes:
        parent (str):
            Required. The relative name of the root
            asset. This can only be an organization number
            (such as "organizations/123"), a project ID
            (such as "projects/my-project-id"), or a project
            number (such as "projects/12345"), or a folder
            number (such as "folders/123").
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp to take an asset snapshot. This can
            only be set to a timestamp between the current
            time and the current time minus 35 days
            (inclusive). If not specified, the current time
            will be used. Due to delays in resource data
            collection and indexing, there is a volatile
            window during which running the same query may
            get different results.
        asset_types (Sequence[str]):
            A list of asset types to take a snapshot for. For example:
            "compute.googleapis.com/Disk".

            Regular expressions are also supported. For example:

            -  "compute.googleapis.com.*" snapshots resources whose
               asset type starts with "compute.googleapis.com".
            -  ".*Instance" snapshots resources whose asset type ends
               with "Instance".
            -  ".*Instance.*" snapshots resources whose asset type
               contains "Instance".

            See `RE2 <https://github.com/google/re2/wiki/Syntax>`__ for
            all supported regular expression syntax. If the regular
            expression does not match any supported asset type, an
            INVALID_ARGUMENT error will be returned.

            If specified, only matching assets will be returned,
            otherwise, it will snapshot all asset types. See
            `Introduction to Cloud Asset
            Inventory <https://cloud.google.com/asset-inventory/docs/overview>`__
            for all supported asset types.
        content_type (google.cloud.asset_v1.types.ContentType):
            Asset content type. If not specified, no
            content but the asset name will be returned.
        output_config (google.cloud.asset_v1.types.OutputConfig):
            Required. Output configuration indicating
            where the results will be output to.
        relationship_types (Sequence[str]):
            A list of relationship types to export, for example:
            ``INSTANCE_TO_INSTANCEGROUP``. This field should only be
            specified if content_type=RELATIONSHIP.

            -  If specified: it snapshots specified relationships. It
               returns an error if any of the [relationship_types]
               doesn't belong to the supported relationship types of the
               [asset_types] or if any of the [asset_types] doesn't
               belong to the source types of the [relationship_types].
            -  Otherwise: it snapshots the supported relationships for
               all [asset_types] or returns an error if any of the
               [asset_types] has no relationship support. An unspecified
               asset types field means all supported asset_types. See
               `Introduction to Cloud Asset
               Inventory <https://cloud.google.com/asset-inventory/docs/overview>`__
               for all supported asset types and relationship types.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    read_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    asset_types = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    content_type = proto.Field(
        proto.ENUM,
        number=4,
        enum="ContentType",
    )
    output_config = proto.Field(
        proto.MESSAGE,
        number=5,
        message="OutputConfig",
    )
    relationship_types = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class ListAssetsRequest(proto.Message):
    r"""ListAssets request.

    Attributes:
        parent (str):
            Required. Name of the organization, folder, or project the
            assets belong to. Format:
            "organizations/[organization-number]" (such as
            "organizations/123"), "projects/[project-id]" (such as
            "projects/my-project-id"), "projects/[project-number]" (such
            as "projects/12345"), or "folders/[folder-number]" (such as
            "folders/12345").
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp to take an asset snapshot. This can
            only be set to a timestamp between the current
            time and the current time minus 35 days
            (inclusive). If not specified, the current time
            will be used. Due to delays in resource data
            collection and indexing, there is a volatile
            window during which running the same query may
            get different results.
        asset_types (Sequence[str]):
            A list of asset types to take a snapshot for. For example:
            "compute.googleapis.com/Disk".

            Regular expression is also supported. For example:

            -  "compute.googleapis.com.*" snapshots resources whose
               asset type starts with "compute.googleapis.com".
            -  ".*Instance" snapshots resources whose asset type ends
               with "Instance".
            -  ".*Instance.*" snapshots resources whose asset type
               contains "Instance".

            See `RE2 <https://github.com/google/re2/wiki/Syntax>`__ for
            all supported regular expression syntax. If the regular
            expression does not match any supported asset type, an
            INVALID_ARGUMENT error will be returned.

            If specified, only matching assets will be returned,
            otherwise, it will snapshot all asset types. See
            `Introduction to Cloud Asset
            Inventory <https://cloud.google.com/asset-inventory/docs/overview>`__
            for all supported asset types.
        content_type (google.cloud.asset_v1.types.ContentType):
            Asset content type. If not specified, no
            content but the asset name will be returned.
        page_size (int):
            The maximum number of assets to be returned
            in a single response. Default is 100, minimum is
            1, and maximum is 1000.
        page_token (str):
            The ``next_page_token`` returned from the previous
            ``ListAssetsResponse``, or unspecified for the first
            ``ListAssetsRequest``. It is a continuation of a prior
            ``ListAssets`` call, and the API should return the next page
            of assets.
        relationship_types (Sequence[str]):
            A list of relationship types to output, for example:
            ``INSTANCE_TO_INSTANCEGROUP``. This field should only be
            specified if content_type=RELATIONSHIP.

            -  If specified: it snapshots specified relationships. It
               returns an error if any of the [relationship_types]
               doesn't belong to the supported relationship types of the
               [asset_types] or if any of the [asset_types] doesn't
               belong to the source types of the [relationship_types].
            -  Otherwise: it snapshots the supported relationships for
               all [asset_types] or returns an error if any of the
               [asset_types] has no relationship support. An unspecified
               asset types field means all supported asset_types. See
               `Introduction to Cloud Asset
               Inventory <https://cloud.google.com/asset-inventory/docs/overview>`__
               for all supported asset types and relationship types.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    read_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    asset_types = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    content_type = proto.Field(
        proto.ENUM,
        number=4,
        enum="ContentType",
    )
    page_size = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token = proto.Field(
        proto.STRING,
        number=6,
    )
    relationship_types = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class BatchGetAssetsHistoryRequest(proto.Message):
    r"""Batch get assets history request.

    Attributes:
        parent (str):
            Required. The relative name of the root
            asset. It can only be an organization number
            (such as "organizations/123"), a project ID
            (such as "projects/my-project-id")", or a
            project number (such as "projects/12345").
        asset_names (Sequence[str]):
            A list of the full names of the assets. See:
            https://cloud.google.com/asset-inventory/docs/resource-name-format
            Example:

            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``.

            The request becomes a no-op if the asset name list is empty,
            and the max size of the asset name list is 100 in one
            request.
        content_type (google.cloud.asset_v1.types.ContentType):
            Optional. The content type.
        read_time_window (google.cloud.asset_v1.types.TimeWindow):
            Optional. The time window for the asset history. Both
            start_time and end_time are optional and if set, it must be
            after the current time minus 35 days. If end_time is not
            set, it is default to current timestamp. If start_time is
            not set, the snapshot of the assets at end_time will be
            returned. The returned results contain all temporal assets
            whose time window overlap with read_time_window.
        relationship_types (Sequence[str]):
            Optional. A list of relationship types to output, for
            example: ``INSTANCE_TO_INSTANCEGROUP``. This field should
            only be specified if content_type=RELATIONSHIP.

            -  If specified: it outputs specified relationships' history
               on the [asset_names]. It returns an error if any of the
               [relationship_types] doesn't belong to the supported
               relationship types of the [asset_names] or if any of the
               [asset_names]'s types doesn't belong to the source types
               of the [relationship_types].
            -  Otherwise: it outputs the supported relationships'
               history on the [asset_names] or returns an error if any
               of the [asset_names]'s types has no relationship support.
               See `Introduction to Cloud Asset
               Inventory <https://cloud.google.com/asset-inventory/docs/overview>`__
               for all supported asset types and relationship types.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_names = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    content_type = proto.Field(
        proto.ENUM,
        number=3,
        enum="ContentType",
    )
    read_time_window = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gca_assets.TimeWindow,
    )
    relationship_types = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class CreateFeedRequest(proto.Message):
    r"""Create asset feed request.

    Attributes:
        parent (str):
            Required. The name of the
            project/folder/organization where this feed
            should be created in. It can only be an
            organization number (such as
            "organizations/123"), a folder number (such as
            "folders/123"), a project ID (such as
            "projects/my-project-id")", or a project number
            (such as "projects/12345").
        feed_id (str):
            Required. This is the client-assigned asset
            feed identifier and it needs to be unique under
            a specific parent project/folder/organization.
        feed (google.cloud.asset_v1.types.Feed):
            Required. The feed details. The field ``name`` must be empty
            and it will be generated in the format of:
            projects/project_number/feeds/feed_id
            folders/folder_number/feeds/feed_id
            organizations/organization_number/feeds/feed_id
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    feed_id = proto.Field(
        proto.STRING,
        number=2,
    )
    feed = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Feed",
    )


class GetFeedRequest(proto.Message):
    r"""Get asset feed request.

    Attributes:
        name (str):
            Required. The name of the Feed and it must be in the format
            of: projects/project_number/feeds/feed_id
            folders/folder_number/feeds/feed_id
            organizations/organization_number/feeds/feed_id
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFeedsRequest(proto.Message):
    r"""List asset feeds request.

    Attributes:
        parent (str):
            Required. The parent
            project/folder/organization whose feeds are to
            be listed. It can only be using
            project/folder/organization number (such as
            "folders/12345")", or a project ID (such as
            "projects/my-project-id").
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateFeedRequest(proto.Message):
    r"""Update asset feed request.

    Attributes:
        feed (google.cloud.asset_v1.types.Feed):
            Required. The new values of feed details. It must match an
            existing feed and the field ``name`` must be in the format
            of: projects/project_number/feeds/feed_id or
            folders/folder_number/feeds/feed_id or
            organizations/organization_number/feeds/feed_id.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Only updates the ``feed`` fields indicated by this
            mask. The field mask must not be empty, and it must not
            contain fields that are immutable or only set by the server.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    feed = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Feed",
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteFeedRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the feed and it must be in the format
            of: projects/project_number/feeds/feed_id
            folders/folder_number/feeds/feed_id
            organizations/organization_number/feeds/feed_id
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class SearchAllResourcesRequest(proto.Message):
    r"""Search all resources request.

    Attributes:
        scope (str):
            Required. A scope can be a project, a folder, or an
            organization. The search is limited to the resources within
            the ``scope``. The caller must be granted the
            ```cloudasset.assets.searchAllResources`` <https://cloud.google.com/asset-inventory/docs/access-control#required_permissions>`__
            permission on the desired scope.

            The allowed values are:

            -  projects/{PROJECT_ID} (e.g., "projects/foo-bar")
            -  projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
            -  folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
            -  organizations/{ORGANIZATION_NUMBER} (e.g.,
               "organizations/123456")
        query (str):
            Optional. The query statement. See `how to construct a
            query <https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query>`__
            for more information. If not specified or empty, it will
            search all the resources within the specified ``scope``.

            Examples:

            -  ``name:Important`` to find Cloud resources whose name
               contains "Important" as a word.
            -  ``name=Important`` to find the Cloud resource whose name
               is exactly "Important".
            -  ``displayName:Impor*`` to find Cloud resources whose
               display name contains "Impor" as a prefix of any word in
               the field.
            -  ``location:us-west*`` to find Cloud resources whose
               location contains both "us" and "west" as prefixes.
            -  ``labels:prod`` to find Cloud resources whose labels
               contain "prod" as a key or value.
            -  ``labels.env:prod`` to find Cloud resources that have a
               label "env" and its value is "prod".
            -  ``labels.env:*`` to find Cloud resources that have a
               label "env".
            -  ``kmsKey:key`` to find Cloud resources encrypted with a
               customer-managed encryption key whose name contains the
               word "key".
            -  ``state:ACTIVE`` to find Cloud resources whose state
               contains "ACTIVE" as a word.
            -  ``NOT state:ACTIVE`` to find Cloud resources whose state
               doesn't contain "ACTIVE" as a word.
            -  ``createTime<1609459200`` to find Cloud resources that
               were created before "2021-01-01 00:00:00 UTC". 1609459200
               is the epoch timestamp of "2021-01-01 00:00:00 UTC" in
               seconds.
            -  ``updateTime>1609459200`` to find Cloud resources that
               were updated after "2021-01-01 00:00:00 UTC". 1609459200
               is the epoch timestamp of "2021-01-01 00:00:00 UTC" in
               seconds.
            -  ``Important`` to find Cloud resources that contain
               "Important" as a word in any of the searchable fields.
            -  ``Impor*`` to find Cloud resources that contain "Impor"
               as a prefix of any word in any of the searchable fields.
            -  ``Important location:(us-west1 OR global)`` to find Cloud
               resources that contain "Important" as a word in any of
               the searchable fields and are also located in the
               "us-west1" region or the "global" location.
        asset_types (Sequence[str]):
            Optional. A list of asset types that this request searches
            for. If empty, it will search all the `searchable asset
            types <https://cloud.google.com/asset-inventory/docs/supported-asset-types#searchable_asset_types>`__.

            Regular expressions are also supported. For example:

            -  "compute.googleapis.com.*" snapshots resources whose
               asset type starts with "compute.googleapis.com".
            -  ".*Instance" snapshots resources whose asset type ends
               with "Instance".
            -  ".*Instance.*" snapshots resources whose asset type
               contains "Instance".

            See `RE2 <https://github.com/google/re2/wiki/Syntax>`__ for
            all supported regular expression syntax. If the regular
            expression does not match any supported asset type, an
            INVALID_ARGUMENT error will be returned.
        page_size (int):
            Optional. The page size for search result pagination. Page
            size is capped at 500 even if a larger value is given. If
            set to zero, server will pick an appropriate default.
            Returned results may be fewer than requested. When this
            happens, there could be more results as long as
            ``next_page_token`` is returned.
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``page_token`` must be the value of ``next_page_token`` from
            the previous response. The values of all other method
            parameters, must be identical to those in the previous call.
        order_by (str):
            Optional. A comma-separated list of fields specifying the
            sorting order of the results. The default order is
            ascending. Add " DESC" after the field name to indicate
            descending order. Redundant space characters are ignored.
            Example: "location DESC, name". Only singular primitive
            fields in the response are sortable:

            -  name
            -  assetType
            -  project
            -  displayName
            -  description
            -  location
            -  kmsKey
            -  createTime
            -  updateTime
            -  state
            -  parentFullResourceName
            -  parentAssetType

            All the other fields such as repeated fields (e.g.,
            ``networkTags``), map fields (e.g., ``labels``) and struct
            fields (e.g., ``additionalAttributes``) are not supported.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A comma-separated list of fields specifying which
            fields to be returned in ResourceSearchResult. Only '*' or
            combination of top level fields can be specified. Field
            names of both snake_case and camelCase are supported.
            Examples: ``"*"``, ``"name,location"``,
            ``"name,versionedResources"``.

            The read_mask paths must be valid field paths listed but not
            limited to (both snake_case and camelCase are supported):

            -  name
            -  assetType
            -  project
            -  displayName
            -  description
            -  location
            -  tagKeys
            -  tagValues
            -  tagValueIds
            -  labels
            -  networkTags
            -  kmsKey
            -  createTime
            -  updateTime
            -  state
            -  additionalAttributes
            -  versionedResources

            If read_mask is not specified, all fields except
            versionedResources will be returned. If only '*' is
            specified, all fields including versionedResources will be
            returned. Any invalid field path will trigger
            INVALID_ARGUMENT error.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    scope = proto.Field(
        proto.STRING,
        number=1,
    )
    query = proto.Field(
        proto.STRING,
        number=2,
    )
    asset_types = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    page_size = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by = proto.Field(
        proto.STRING,
        number=6,
    )
    read_mask = proto.Field(
        proto.MESSAGE,
        number=8,
        message=field_mask_pb2.FieldMask,
    )


class SearchAllIamPoliciesRequest(proto.Message):
    r"""Search all IAM policies request.

    Attributes:
        scope (str):
            Required. A scope can be a project, a folder, or an
            organization. The search is limited to the IAM policies
            within the ``scope``. The caller must be granted the
            ```cloudasset.assets.searchAllIamPolicies`` <https://cloud.google.com/asset-inventory/docs/access-control#required_permissions>`__
            permission on the desired scope.

            The allowed values are:

            -  projects/{PROJECT_ID} (e.g., "projects/foo-bar")
            -  projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
            -  folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
            -  organizations/{ORGANIZATION_NUMBER} (e.g.,
               "organizations/123456")
        query (str):
            Optional. The query statement. See `how to construct a
            query <https://cloud.google.com/asset-inventory/docs/searching-iam-policies#how_to_construct_a_query>`__
            for more information. If not specified or empty, it will
            search all the IAM policies within the specified ``scope``.
            Note that the query string is compared against each Cloud
            IAM policy binding, including its principals, roles, and
            Cloud IAM conditions. The returned Cloud IAM policies will
            only contain the bindings that match your query. To learn
            more about the IAM policy structure, see `IAM policy
            doc <https://cloud.google.com/iam/docs/policies#structure>`__.

            Examples:

            -  ``policy:amy@gmail.com`` to find IAM policy bindings that
               specify user "amy@gmail.com".
            -  ``policy:roles/compute.admin`` to find IAM policy
               bindings that specify the Compute Admin role.
            -  ``policy:comp*`` to find IAM policy bindings that contain
               "comp" as a prefix of any word in the binding.
            -  ``policy.role.permissions:storage.buckets.update`` to
               find IAM policy bindings that specify a role containing
               "storage.buckets.update" permission. Note that if callers
               don't have ``iam.roles.get`` access to a role's included
               permissions, policy bindings that specify this role will
               be dropped from the search results.
            -  ``policy.role.permissions:upd*`` to find IAM policy
               bindings that specify a role containing "upd" as a prefix
               of any word in the role permission. Note that if callers
               don't have ``iam.roles.get`` access to a role's included
               permissions, policy bindings that specify this role will
               be dropped from the search results.
            -  ``resource:organizations/123456`` to find IAM policy
               bindings that are set on "organizations/123456".
            -  ``resource=//cloudresourcemanager.googleapis.com/projects/myproject``
               to find IAM policy bindings that are set on the project
               named "myproject".
            -  ``Important`` to find IAM policy bindings that contain
               "Important" as a word in any of the searchable fields
               (except for the included permissions).
            -  ``resource:(instance1 OR instance2) policy:amy`` to find
               IAM policy bindings that are set on resources "instance1"
               or "instance2" and also specify user "amy".
            -  ``roles:roles/compute.admin`` to find IAM policy bindings
               that specify the Compute Admin role.
            -  ``memberTypes:user`` to find IAM policy bindings that
               contain the principal type "user".
        page_size (int):
            Optional. The page size for search result pagination. Page
            size is capped at 500 even if a larger value is given. If
            set to zero, server will pick an appropriate default.
            Returned results may be fewer than requested. When this
            happens, there could be more results as long as
            ``next_page_token`` is returned.
        page_token (str):
            Optional. If present, retrieve the next batch of results
            from the preceding call to this method. ``page_token`` must
            be the value of ``next_page_token`` from the previous
            response. The values of all other method parameters must be
            identical to those in the previous call.
        asset_types (Sequence[str]):
            Optional. A list of asset types that the IAM policies are
            attached to. If empty, it will search the IAM policies that
            are attached to all the `searchable asset
            types <https://cloud.google.com/asset-inventory/docs/supported-asset-types#searchable_asset_types>`__.

            Regular expressions are also supported. For example:

            -  "compute.googleapis.com.*" snapshots IAM policies
               attached to asset type starts with
               "compute.googleapis.com".
            -  ".*Instance" snapshots IAM policies attached to asset
               type ends with "Instance".
            -  ".*Instance.*" snapshots IAM policies attached to asset
               type contains "Instance".

            See `RE2 <https://github.com/google/re2/wiki/Syntax>`__ for
            all supported regular expression syntax. If the regular
            expression does not match any supported asset type, an
            INVALID_ARGUMENT error will be returned.
        order_by (str):
            Optional. A comma-separated list of fields specifying the
            sorting order of the results. The default order is
            ascending. Add " DESC" after the field name to indicate
            descending order. Redundant space characters are ignored.
            Example: "assetType DESC, resource". Only singular primitive
            fields in the response are sortable:

            -  resource
            -  assetType
            -  project All the other fields such as repeated fields
               (e.g., ``folders``) and non-primitive fields (e.g.,
               ``policy``) are not supported.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    scope = proto.Field(
        proto.STRING,
        number=1,
    )
    query = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token = proto.Field(
        proto.STRING,
        number=4,
    )
    asset_types = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    order_by = proto.Field(
        proto.STRING,
        number=7,
    )


class AnalyzeIamPolicyRequest(proto.Message):
    r"""A request message for
    [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1.AssetService.AnalyzeIamPolicy].

    Attributes:
        analysis_query (google.cloud.asset_v1.types.IamPolicyAnalysisQuery):
            Required. The request query.
        saved_analysis_query (str):
            Optional. The name of a saved query, which must be in the
            format of:

            -  projects/project_number/savedQueries/saved_query_id
            -  folders/folder_number/savedQueries/saved_query_id
            -  organizations/organization_number/savedQueries/saved_query_id

            If both ``analysis_query`` and ``saved_analysis_query`` are
            provided, they will be merged together with the
            ``saved_analysis_query`` as base and the ``analysis_query``
            as overrides. For more details of the merge behavior, please
            refer to the
            `MergeFrom <https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details>`__
            page.

            Note that you cannot override primitive fields with default
            value, such as 0 or empty string, etc., because we use
            proto3, which doesn't support field presence yet.
        execution_timeout (google.protobuf.duration_pb2.Duration):
            Optional. Amount of time executable has to complete. See
            JSON representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__.

            If this field is set with a value less than the RPC
            deadline, and the execution of your query hasn't finished in
            the specified execution timeout, you will get a response
            with partial result. Otherwise, your query's execution will
            continue until the RPC deadline. If it's not finished until
            then, you will get a DEADLINE_EXCEEDED error.

            Default is empty.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    analysis_query = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IamPolicyAnalysisQuery",
    )
    saved_analysis_query = proto.Field(
        proto.STRING,
        number=3,
    )
    execution_timeout = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class AnalyzeIamPolicyLongrunningRequest(proto.Message):
    r"""A request message for
    [AssetService.AnalyzeIamPolicyLongrunning][google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning].

    Attributes:
        analysis_query (google.cloud.asset_v1.types.IamPolicyAnalysisQuery):
            Required. The request query.
        saved_analysis_query (str):
            Optional. The name of a saved query, which must be in the
            format of:

            -  projects/project_number/savedQueries/saved_query_id
            -  folders/folder_number/savedQueries/saved_query_id
            -  organizations/organization_number/savedQueries/saved_query_id

            If both ``analysis_query`` and ``saved_analysis_query`` are
            provided, they will be merged together with the
            ``saved_analysis_query`` as base and the ``analysis_query``
            as overrides. For more details of the merge behavior, please
            refer to the
            `MergeFrom <https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details>`__
            doc.

            Note that you cannot override primitive fields with default
            value, such as 0 or empty string, etc., because we use
            proto3, which doesn't support field presence yet.
        output_config (google.cloud.asset_v1.types.IamPolicyAnalysisOutputConfig):
            Required. Output configuration indicating
            where the results will be output to.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    analysis_query = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IamPolicyAnalysisQuery",
    )
    saved_analysis_query = proto.Field(
        proto.STRING,
        number=3,
    )
    output_config = proto.Field(
        proto.MESSAGE,
        number=2,
        message="IamPolicyAnalysisOutputConfig",
    )


class CreateSavedQueryRequest(proto.Message):
    r"""Request to create a saved query.

    Attributes:
        parent (str):
            Required. The name of the project/folder/organization where
            this saved_query should be created in. It can only be an
            organization number (such as "organizations/123"), a folder
            number (such as "folders/123"), a project ID (such as
            "projects/my-project-id")", or a project number (such as
            "projects/12345").
        saved_query (google.cloud.asset_v1.types.SavedQuery):
            Required. The saved_query details. The ``name`` field must
            be empty as it will be generated based on the parent and
            saved_query_id.
        saved_query_id (str):
            Required. The ID to use for the saved query, which must be
            unique in the specified parent. It will become the final
            component of the saved query's resource name.

            This value should be 4-63 characters, and valid characters
            are /[a-z][0-9]-/.

            Notice that this field is required in the saved query
            creation, and the ``name`` field of the ``saved_query`` will
            be ignored.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    saved_query = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SavedQuery",
    )
    saved_query_id = proto.Field(
        proto.STRING,
        number=3,
    )


class GetSavedQueryRequest(proto.Message):
    r"""Request to get a saved query.

    Attributes:
        name (str):
            Required. The name of the saved query and it must be in the
            format of:

            -  projects/project_number/savedQueries/saved_query_id
            -  folders/folder_number/savedQueries/saved_query_id
            -  organizations/organization_number/savedQueries/saved_query_id
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSavedQueriesRequest(proto.Message):
    r"""Request to list saved queries.

    Attributes:
        parent (str):
            Required. The parent
            project/folder/organization whose savedQueries
            are to be listed. It can only be using
            project/folder/organization number (such as
            "folders/12345")", or a project ID (such as
            "projects/my-project-id").
        filter (str):
            Optional. The expression to filter resources. The expression
            is a list of zero or more restrictions combined via logical
            operators ``AND`` and ``OR``. When ``AND`` and ``OR`` are
            both used in the expression, parentheses must be
            appropriately used to group the combinations. The expression
            may also contain regular expressions.

            See https://google.aip.dev/160 for more information on the
            grammar.
        page_size (int):
            Optional. The maximum number of saved queries
            to return per page. The service may return fewer
            than this value. If unspecified, at most 50 will
            be returned.
             The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSavedQueries`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListSavedQueries`` must match the call that provided the
            page token.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    filter = proto.Field(
        proto.STRING,
        number=4,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateSavedQueryRequest(proto.Message):
    r"""Request to update a saved query.

    Attributes:
        saved_query (google.cloud.asset_v1.types.SavedQuery):
            Required. The saved query to update.

            The saved query's ``name`` field is used to identify the one
            to update, which has format as below:

            -  projects/project_number/savedQueries/saved_query_id
            -  folders/folder_number/savedQueries/saved_query_id
            -  organizations/organization_number/savedQueries/saved_query_id
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    saved_query = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SavedQuery",
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSavedQueryRequest(proto.Message):
    r"""Request to delete a saved query.

    Attributes:
        name (str):
            Required. The name of the saved query to delete. It must be
            in the format of:

            -  projects/project_number/savedQueries/saved_query_id
            -  folders/folder_number/savedQueries/saved_query_id
            -  organizations/organization_number/savedQueries/saved_query_id
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class AnalyzeMoveRequest(proto.Message):
    r"""The request message for performing resource move analysis.

    Attributes:
        resource (str):
            Required. Name of the resource to perform the
            analysis against. Only GCP Project are supported
            as of today. Hence, this can only be Project ID
            (such as "projects/my-project-id") or a Project
            Number (such as "projects/12345").
        destination_parent (str):
            Required. Name of the GCP Folder or
            Organization to reparent the target resource.
            The analysis will be performed against
            hypothetically moving the resource to this
            specified desitination parent. This can only be
            a Folder number (such as "folders/123") or an
            Organization number (such as
            "organizations/123").
        view (google.cloud.asset_v1.types.AnalyzeMoveRequest.AnalysisView):
            Analysis view indicating what information
            should be included in the analysis response. If
            unspecified, the default view is FULL.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    class AnalysisView(proto.Enum):
        r"""View enum for supporting partial analysis responses."""
        __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore
        ANALYSIS_VIEW_UNSPECIFIED = 0
        FULL = 1
        BASIC = 2

    resource = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_parent = proto.Field(
        proto.STRING,
        number=2,
    )
    view = proto.Field(
        proto.ENUM,
        number=3,
        enum=AnalysisView,
    )


class BatchGetEffectiveIamPoliciesRequest(proto.Message):
    r"""A request message for
    [AssetService.BatchGetEffectiveIamPolicies][google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies].

    Attributes:
        scope (str):
            Required. Only IAM policies on or below the scope will be
            returned.

            This can only be an organization number (such as
            "organizations/123"), a folder number (such as
            "folders/123"), a project ID (such as
            "projects/my-project-id"), or a project number (such as
            "projects/12345").

            To know how to get organization id, visit
            `here <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>`__.

            To know how to get folder or project id, visit
            `here <https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects>`__.
        names (Sequence[str]):
            Required. The names refer to the [full_resource_names]
            (https://cloud.google.com/asset-inventory/docs/resource-name-format)
            of `searchable asset
            types <https://cloud.google.com/asset-inventory/docs/supported-asset-types#searchable_asset_types>`__.
            A maximum of 20 resources' effective policies can be
            retrieved in a batch.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    scope = proto.Field(
        proto.STRING,
        number=1,
    )
    names = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__manifest__))
