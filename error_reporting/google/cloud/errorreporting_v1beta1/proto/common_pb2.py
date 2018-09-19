# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/clouderrorreporting_v1beta1/proto/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/clouderrorreporting_v1beta1/proto/common.proto',
  package='google.devtools.clouderrorreporting.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n>google/devtools/clouderrorreporting_v1beta1/proto/common.proto\x12+google.devtools.clouderrorreporting.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a#google/api/monitored_resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x81\x01\n\nErrorGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12S\n\x0ftracking_issues\x18\x03 \x03(\x0b\x32:.google.devtools.clouderrorreporting.v1beta1.TrackingIssue\"\x1c\n\rTrackingIssue\x12\x0b\n\x03url\x18\x01 \x01(\t\"\xef\x01\n\nErrorEvent\x12.\n\nevent_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12T\n\x0fservice_context\x18\x02 \x01(\x0b\x32;.google.devtools.clouderrorreporting.v1beta1.ServiceContext\x12\x0f\n\x07message\x18\x03 \x01(\t\x12J\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\x39.google.devtools.clouderrorreporting.v1beta1.ErrorContext\"I\n\x0eServiceContext\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x15\n\rresource_type\x18\x04 \x01(\t\"\xc9\x01\n\x0c\x45rrorContext\x12U\n\x0chttp_request\x18\x01 \x01(\x0b\x32?.google.devtools.clouderrorreporting.v1beta1.HttpRequestContext\x12\x0c\n\x04user\x18\x02 \x01(\t\x12T\n\x0freport_location\x18\x03 \x01(\x0b\x32;.google.devtools.clouderrorreporting.v1beta1.SourceLocation\"\x88\x01\n\x12HttpRequestContext\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x12\n\nuser_agent\x18\x03 \x01(\t\x12\x10\n\x08referrer\x18\x04 \x01(\t\x12\x1c\n\x14response_status_code\x18\x05 \x01(\x05\x12\x11\n\tremote_ip\x18\x06 \x01(\t\"O\n\x0eSourceLocation\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x13\n\x0bline_number\x18\x02 \x01(\x05\x12\x15\n\rfunction_name\x18\x04 \x01(\tB\xec\x01\n/com.google.devtools.clouderrorreporting.v1beta1B\x0b\x43ommonProtoP\x01Z^google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1;clouderrorreporting\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_monitored__resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ERRORGROUP = _descriptor.Descriptor(
  name='ErrorGroup',
  full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroup.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroup.group_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracking_issues', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroup.tracking_issues', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=341,
)


_TRACKINGISSUE = _descriptor.Descriptor(
  name='TrackingIssue',
  full_name='google.devtools.clouderrorreporting.v1beta1.TrackingIssue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='google.devtools.clouderrorreporting.v1beta1.TrackingIssue.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=343,
  serialized_end=371,
)


_ERROREVENT = _descriptor.Descriptor(
  name='ErrorEvent',
  full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_time', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent.event_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_context', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent.service_context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent.context', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=613,
)


_SERVICECONTEXT = _descriptor.Descriptor(
  name='ServiceContext',
  full_name='google.devtools.clouderrorreporting.v1beta1.ServiceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='google.devtools.clouderrorreporting.v1beta1.ServiceContext.service', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='google.devtools.clouderrorreporting.v1beta1.ServiceContext.version', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='google.devtools.clouderrorreporting.v1beta1.ServiceContext.resource_type', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=615,
  serialized_end=688,
)


_ERRORCONTEXT = _descriptor.Descriptor(
  name='ErrorContext',
  full_name='google.devtools.clouderrorreporting.v1beta1.ErrorContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_request', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorContext.http_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorContext.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='report_location', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorContext.report_location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=691,
  serialized_end=892,
)


_HTTPREQUESTCONTEXT = _descriptor.Descriptor(
  name='HttpRequestContext',
  full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_agent', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.user_agent', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referrer', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.referrer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_status_code', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.response_status_code', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_ip', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.remote_ip', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=1031,
)


_SOURCELOCATION = _descriptor.Descriptor(
  name='SourceLocation',
  full_name='google.devtools.clouderrorreporting.v1beta1.SourceLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_path', full_name='google.devtools.clouderrorreporting.v1beta1.SourceLocation.file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line_number', full_name='google.devtools.clouderrorreporting.v1beta1.SourceLocation.line_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function_name', full_name='google.devtools.clouderrorreporting.v1beta1.SourceLocation.function_name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1033,
  serialized_end=1112,
)

_ERRORGROUP.fields_by_name['tracking_issues'].message_type = _TRACKINGISSUE
_ERROREVENT.fields_by_name['event_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ERROREVENT.fields_by_name['service_context'].message_type = _SERVICECONTEXT
_ERROREVENT.fields_by_name['context'].message_type = _ERRORCONTEXT
_ERRORCONTEXT.fields_by_name['http_request'].message_type = _HTTPREQUESTCONTEXT
_ERRORCONTEXT.fields_by_name['report_location'].message_type = _SOURCELOCATION
DESCRIPTOR.message_types_by_name['ErrorGroup'] = _ERRORGROUP
DESCRIPTOR.message_types_by_name['TrackingIssue'] = _TRACKINGISSUE
DESCRIPTOR.message_types_by_name['ErrorEvent'] = _ERROREVENT
DESCRIPTOR.message_types_by_name['ServiceContext'] = _SERVICECONTEXT
DESCRIPTOR.message_types_by_name['ErrorContext'] = _ERRORCONTEXT
DESCRIPTOR.message_types_by_name['HttpRequestContext'] = _HTTPREQUESTCONTEXT
DESCRIPTOR.message_types_by_name['SourceLocation'] = _SOURCELOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorGroup = _reflection.GeneratedProtocolMessageType('ErrorGroup', (_message.Message,), dict(
  DESCRIPTOR = _ERRORGROUP,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.common_pb2'
  ,
  __doc__ = """Description of a group of similar error events.
  
  
  Attributes:
      name:
          The group resource name. Example: projects/my-
          project-123/groups/my-groupid
      group_id:
          Group IDs are unique for a given project. If the same kind of
          error occurs in different service contexts, it will receive
          the same group ID.
      tracking_issues:
          Associated tracking issues.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ErrorGroup)
  ))
_sym_db.RegisterMessage(ErrorGroup)

TrackingIssue = _reflection.GeneratedProtocolMessageType('TrackingIssue', (_message.Message,), dict(
  DESCRIPTOR = _TRACKINGISSUE,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.common_pb2'
  ,
  __doc__ = """Information related to tracking the progress on resolving the error.
  
  
  Attributes:
      url:
          A URL pointing to a related entry in an issue tracking system.
          Example: https://github.com/user/project/issues/4
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.TrackingIssue)
  ))
_sym_db.RegisterMessage(TrackingIssue)

ErrorEvent = _reflection.GeneratedProtocolMessageType('ErrorEvent', (_message.Message,), dict(
  DESCRIPTOR = _ERROREVENT,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.common_pb2'
  ,
  __doc__ = """An error event which is returned by the Error Reporting system.
  
  
  Attributes:
      event_time:
          Time when the event occurred as provided in the error report.
          If the report did not contain a timestamp, the time the error
          was received by the Error Reporting system is used.
      service_context:
          The ``ServiceContext`` for which this error was reported.
      message:
          The stack trace that was reported or logged by the service.
      context:
          Data about the context in which the error occurred.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ErrorEvent)
  ))
_sym_db.RegisterMessage(ErrorEvent)

ServiceContext = _reflection.GeneratedProtocolMessageType('ServiceContext', (_message.Message,), dict(
  DESCRIPTOR = _SERVICECONTEXT,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.common_pb2'
  ,
  __doc__ = """Describes a running service that sends errors. Its version changes over
  time and multiple versions can run in parallel.
  
  
  Attributes:
      service:
          An identifier of the service, such as the name of the
          executable, job, or Google App Engine service name. This field
          is expected to have a low number of values that are relatively
          stable over time, as opposed to ``version``, which can be
          changed whenever new code is deployed.  Contains the service
          name for error reports extracted from Google App Engine logs
          or ``default`` if the App Engine default service is used.
      version:
          Represents the source code version that the developer
          provided, which could represent a version label or a Git SHA-1
          hash, for example.
      resource_type:
          Type of the MonitoredResource. List of possible values:
          https://cloud.google.com/monitoring/api/resources  Value is
          set automatically for incoming errors and must not be set when
          reporting errors.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ServiceContext)
  ))
_sym_db.RegisterMessage(ServiceContext)

ErrorContext = _reflection.GeneratedProtocolMessageType('ErrorContext', (_message.Message,), dict(
  DESCRIPTOR = _ERRORCONTEXT,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.common_pb2'
  ,
  __doc__ = """A description of the context in which an error occurred. This data
  should be provided by the application when reporting an error, unless
  the error report has been generated automatically from Google App Engine
  logs.
  
  
  Attributes:
      http_request:
          The HTTP request which was processed when the error was
          triggered.
      user:
          The user who caused or was affected by the crash. This can be
          a user ID, an email address, or an arbitrary token that
          uniquely identifies the user. When sending an error report,
          leave this field empty if the user was not logged in. In this
          case the Error Reporting system will use other data, such as
          remote IP address, to distinguish affected users. See
          ``affected_users_count`` in ``ErrorGroupStats``.
      report_location:
          The location in the source code where the decision was made to
          report the error, usually the place where it was logged. For a
          logged exception this would be the source line where the
          exception is logged, usually close to the place where it was
          caught. This value is in contrast to
          ``Exception.cause_location``, which describes the source line
          where the exception was thrown.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ErrorContext)
  ))
_sym_db.RegisterMessage(ErrorContext)

HttpRequestContext = _reflection.GeneratedProtocolMessageType('HttpRequestContext', (_message.Message,), dict(
  DESCRIPTOR = _HTTPREQUESTCONTEXT,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.common_pb2'
  ,
  __doc__ = """HTTP request data that is related to a reported error. This data should
  be provided by the application when reporting an error, unless the error
  report has been generated automatically from Google App Engine logs.
  
  
  Attributes:
      method:
          The type of HTTP request, such as ``GET``, ``POST``, etc.
      url:
          The URL of the request.
      user_agent:
          The user agent information that is provided with the request.
      referrer:
          The referrer information that is provided with the request.
      response_status_code:
          The HTTP response status code for the request.
      remote_ip:
          The IP address from which the request originated. This can be
          IPv4, IPv6, or a token which is derived from the IP address,
          depending on the data that has been provided in the error
          report.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.HttpRequestContext)
  ))
_sym_db.RegisterMessage(HttpRequestContext)

SourceLocation = _reflection.GeneratedProtocolMessageType('SourceLocation', (_message.Message,), dict(
  DESCRIPTOR = _SOURCELOCATION,
  __module__ = 'google.devtools.clouderrorreporting_v1beta1.proto.common_pb2'
  ,
  __doc__ = """Indicates a location in the source code of the service for which errors
  are reported. This data should be provided by the application when
  reporting an error, unless the error report has been generated
  automatically from Google App Engine logs. All fields are optional.
  
  
  Attributes:
      file_path:
          The source code filename, which can include a truncated
          relative path, or a full path from a production machine.
      line_number:
          1-based. 0 indicates that the line number is unknown.
      function_name:
          Human-readable name of a function or method. The value can
          include optional context like the class or package name. For
          example, ``my.package.MyClass.method`` in case of Java.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.SourceLocation)
  ))
_sym_db.RegisterMessage(SourceLocation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n/com.google.devtools.clouderrorreporting.v1beta1B\013CommonProtoP\001Z^google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1;clouderrorreporting\252\002#Google.Cloud.ErrorReporting.V1Beta1\312\002#Google\\Cloud\\ErrorReporting\\V1beta1'))
# @@protoc_insertion_point(module_scope)