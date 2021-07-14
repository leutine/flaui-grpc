# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flaui.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='flaui.proto',
  package='flarpc',
  syntax='proto3',
  serialized_options=b'\252\002\006Server',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x66laui.proto\x12\x06\x66larpc\"\x1b\n\x0b\x41pplication\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"/\n\x0eTypeTextObject\x12\x0f\n\x07\x65lement\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t2|\n\x06\x46laRPC\x12\x32\n\x06Launch\x12\x13.flarpc.Application\x1a\x13.flarpc.Application\x12>\n\x0cTestTypeText\x12\x16.flarpc.TypeTextObject\x1a\x16.flarpc.TypeTextObjectB\t\xaa\x02\x06Serverb\x06proto3'
)




_APPLICATION = _descriptor.Descriptor(
  name='Application',
  full_name='flarpc.Application',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='flarpc.Application.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=50,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='flarpc.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=59,
)


_TYPETEXTOBJECT = _descriptor.Descriptor(
  name='TypeTextObject',
  full_name='flarpc.TypeTextObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='flarpc.TypeTextObject.element', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='flarpc.TypeTextObject.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['Application'] = _APPLICATION
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['TypeTextObject'] = _TYPETEXTOBJECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Application = _reflection.GeneratedProtocolMessageType('Application', (_message.Message,), {
  'DESCRIPTOR' : _APPLICATION,
  '__module__' : 'flaui_pb2'
  # @@protoc_insertion_point(class_scope:flarpc.Application)
  })
_sym_db.RegisterMessage(Application)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'flaui_pb2'
  # @@protoc_insertion_point(class_scope:flarpc.Empty)
  })
_sym_db.RegisterMessage(Empty)

TypeTextObject = _reflection.GeneratedProtocolMessageType('TypeTextObject', (_message.Message,), {
  'DESCRIPTOR' : _TYPETEXTOBJECT,
  '__module__' : 'flaui_pb2'
  # @@protoc_insertion_point(class_scope:flarpc.TypeTextObject)
  })
_sym_db.RegisterMessage(TypeTextObject)


DESCRIPTOR._options = None

_FLARPC = _descriptor.ServiceDescriptor(
  name='FlaRPC',
  full_name='flarpc.FlaRPC',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=110,
  serialized_end=234,
  methods=[
  _descriptor.MethodDescriptor(
    name='Launch',
    full_name='flarpc.FlaRPC.Launch',
    index=0,
    containing_service=None,
    input_type=_APPLICATION,
    output_type=_APPLICATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestTypeText',
    full_name='flarpc.FlaRPC.TestTypeText',
    index=1,
    containing_service=None,
    input_type=_TYPETEXTOBJECT,
    output_type=_TYPETEXTOBJECT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FLARPC)

DESCRIPTOR.services_by_name['FlaRPC'] = _FLARPC

# @@protoc_insertion_point(module_scope)
