# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: world.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bworld.proto\x12\x0c\x61igame.world\x1a\x19google/protobuf/any.proto\"A\n\tWorldArea\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x05\x61reas\x18\x02 \x03(\x0b\x32\x17.aigame.world.WorldArea\"\xd4\x01\n\x10\x43reateWorldQuery\x12\x10\n\x08world_id\x18\x01 \x01(\x05\x12\x11\n\tworld_key\x18\x02 \x01(\x03\x12&\n\x05\x61reas\x18\x03 \x01(\x0b\x32\x17.aigame.world.WorldArea\x12=\n\tnpc_datas\x18\x04 \x03(\x0b\x32*.aigame.world.CreateWorldQuery.NPCInitData\x1a\x34\n\x0bNPCInitData\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\x03\x12\x0c\n\x04\x61rea\x18\x03 \x01(\t\"\xd0\x01\n\x10\x43reateWorldReply\x12\x11\n\tworld_key\x18\x01 \x01(\x03\x12&\n\x05\x61reas\x18\x02 \x01(\x0b\x32\x17.aigame.world.WorldArea\x12?\n\nnpc_orders\x18\x03 \x03(\x0b\x32+.aigame.world.CreateWorldReply.NPCInitOrder\x1a@\n\x0cNPCInitOrder\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12#\n\x05order\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"1\n\x0eHeartBeatQuery\x12\x11\n\tworld_key\x18\x01 \x01(\x03\x12\x0c\n\x04time\x18\x02 \x01(\x03\"1\n\x0eHeartBeatReply\x12\x11\n\tworld_key\x18\x01 \x01(\x03\x12\x0c\n\x04time\x18\x02 \x01(\x03\"C\n\rEndWorldQuery\x12\x11\n\tworld_key\x18\x01 \x01(\x03\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x0f\n\x07success\x18\x03 \x01(\x08\"C\n\rEndWorldReply\x12\x11\n\tworld_key\x18\x01 \x01(\x03\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x0f\n\x07success\x18\x03 \x01(\x08\x42\x02P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'world_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'P\001'
  _globals['_WORLDAREA']._serialized_start=56
  _globals['_WORLDAREA']._serialized_end=121
  _globals['_CREATEWORLDQUERY']._serialized_start=124
  _globals['_CREATEWORLDQUERY']._serialized_end=336
  _globals['_CREATEWORLDQUERY_NPCINITDATA']._serialized_start=284
  _globals['_CREATEWORLDQUERY_NPCINITDATA']._serialized_end=336
  _globals['_CREATEWORLDREPLY']._serialized_start=339
  _globals['_CREATEWORLDREPLY']._serialized_end=547
  _globals['_CREATEWORLDREPLY_NPCINITORDER']._serialized_start=483
  _globals['_CREATEWORLDREPLY_NPCINITORDER']._serialized_end=547
  _globals['_HEARTBEATQUERY']._serialized_start=549
  _globals['_HEARTBEATQUERY']._serialized_end=598
  _globals['_HEARTBEATREPLY']._serialized_start=600
  _globals['_HEARTBEATREPLY']._serialized_end=649
  _globals['_ENDWORLDQUERY']._serialized_start=651
  _globals['_ENDWORLDQUERY']._serialized_end=718
  _globals['_ENDWORLDREPLY']._serialized_start=720
  _globals['_ENDWORLDREPLY']._serialized_end=787
# @@protoc_insertion_point(module_scope)