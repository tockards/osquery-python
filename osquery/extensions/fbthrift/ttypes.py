#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from __future__ import absolute_import
import six
from thrift.util.Recursive import fix_spec
from thrift.Thrift import *
from thrift.protocol.TProtocol import TProtocolException



import pprint
import warnings
from thrift import Thrift
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.protocol import THeaderProtocol
try:
  from thrift.protocol import fastproto
except:
  fastproto = None
all_structs = []
UTF8STRINGS = bool(0) or sys.version_info.major >= 3

__all__ = ['UTF8STRINGS', 'ExtensionCode', 'InternalOptionInfo', 'InternalExtensionInfo', 'ExtensionStatus', 'ExtensionResponse', 'ExtensionException']

class ExtensionCode:
  EXT_SUCCESS = 0
  EXT_FAILED = 1
  EXT_FATAL = 2

  _VALUES_TO_NAMES = {
    0: "EXT_SUCCESS",
    1: "EXT_FAILED",
    2: "EXT_FATAL",
  }

  _NAMES_TO_VALUES = {
    "EXT_SUCCESS": 0,
    "EXT_FAILED": 1,
    "EXT_FATAL": 2,
  }

class InternalOptionInfo:
  """
  Attributes:
   - value
   - default_value
   - type
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      self.checkRequired()
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      self.checkRequired()
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.value = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.default_value = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.type = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()
    self.checkRequired()

  def checkRequired(self):
    return

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('InternalOptionInfo')
    if self.value != None:
      oprot.writeFieldBegin('value', TType.STRING, 1)
      oprot.writeString(self.value.encode('utf-8')) if UTF8STRINGS and not isinstance(self.value, bytes) else oprot.writeString(self.value)
      oprot.writeFieldEnd()
    if self.default_value != None:
      oprot.writeFieldBegin('default_value', TType.STRING, 2)
      oprot.writeString(self.default_value.encode('utf-8')) if UTF8STRINGS and not isinstance(self.default_value, bytes) else oprot.writeString(self.default_value)
      oprot.writeFieldEnd()
    if self.type != None:
      oprot.writeFieldBegin('type', TType.STRING, 3)
      oprot.writeString(self.type.encode('utf-8')) if UTF8STRINGS and not isinstance(self.type, bytes) else oprot.writeString(self.type)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    padding = ' ' * 4
    value = pprint.pformat(self.value, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    value=%s' % (value))
    value = pprint.pformat(self.default_value, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    default_value=%s' % (value))
    value = pprint.pformat(self.type, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    type=%s' % (value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

class InternalExtensionInfo:
  """
  Attributes:
   - name
   - version
   - sdk_version
   - min_sdk_version
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      self.checkRequired()
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      self.checkRequired()
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.version = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.sdk_version = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.min_sdk_version = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()
    self.checkRequired()

  def checkRequired(self):
    return

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('InternalExtensionInfo')
    if self.name != None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name.encode('utf-8')) if UTF8STRINGS and not isinstance(self.name, bytes) else oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.version != None:
      oprot.writeFieldBegin('version', TType.STRING, 2)
      oprot.writeString(self.version.encode('utf-8')) if UTF8STRINGS and not isinstance(self.version, bytes) else oprot.writeString(self.version)
      oprot.writeFieldEnd()
    if self.sdk_version != None:
      oprot.writeFieldBegin('sdk_version', TType.STRING, 3)
      oprot.writeString(self.sdk_version.encode('utf-8')) if UTF8STRINGS and not isinstance(self.sdk_version, bytes) else oprot.writeString(self.sdk_version)
      oprot.writeFieldEnd()
    if self.min_sdk_version != None:
      oprot.writeFieldBegin('min_sdk_version', TType.STRING, 4)
      oprot.writeString(self.min_sdk_version.encode('utf-8')) if UTF8STRINGS and not isinstance(self.min_sdk_version, bytes) else oprot.writeString(self.min_sdk_version)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    padding = ' ' * 4
    value = pprint.pformat(self.name, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    name=%s' % (value))
    value = pprint.pformat(self.version, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    version=%s' % (value))
    value = pprint.pformat(self.sdk_version, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    sdk_version=%s' % (value))
    value = pprint.pformat(self.min_sdk_version, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    min_sdk_version=%s' % (value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

class ExtensionStatus:
  """
  Attributes:
   - code
   - message
   - uuid
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      self.checkRequired()
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      self.checkRequired()
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.code = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.message = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.uuid = iprot.readI64()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()
    self.checkRequired()

  def checkRequired(self):
    return

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('ExtensionStatus')
    if self.code != None:
      oprot.writeFieldBegin('code', TType.I32, 1)
      oprot.writeI32(self.code)
      oprot.writeFieldEnd()
    if self.message != None:
      oprot.writeFieldBegin('message', TType.STRING, 2)
      oprot.writeString(self.message.encode('utf-8')) if UTF8STRINGS and not isinstance(self.message, bytes) else oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.uuid != None:
      oprot.writeFieldBegin('uuid', TType.I64, 3)
      oprot.writeI64(self.uuid)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    padding = ' ' * 4
    value = pprint.pformat(self.code, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    code=%s' % (value))
    value = pprint.pformat(self.message, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    message=%s' % (value))
    value = pprint.pformat(self.uuid, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    uuid=%s' % (value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

class ExtensionResponse:
  """
  Attributes:
   - status
   - response
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      self.checkRequired()
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      self.checkRequired()
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = ExtensionStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.response = []
          (_etype3, _size0) = iprot.readListBegin()
          if _size0 >= 0:
            for _i4 in six.moves.range(_size0):
              _elem5 = {}
              (_ktype7, _vtype8, _size6 ) = iprot.readMapBegin() 
              if _size6 >= 0:
                for _i10 in six.moves.range(_size6):
                  _key11 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
                  _val12 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
                  _elem5[_key11] = _val12
              else: 
                while iprot.peekMap():
                  _key13 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
                  _val14 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
                  _elem5[_key13] = _val14
              iprot.readMapEnd()
              self.response.append(_elem5)
          else: 
            while iprot.peekList():
              _elem15 = {}
              (_ktype17, _vtype18, _size16 ) = iprot.readMapBegin() 
              if _size16 >= 0:
                for _i20 in six.moves.range(_size16):
                  _key21 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
                  _val22 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
                  _elem15[_key21] = _val22
              else: 
                while iprot.peekMap():
                  _key23 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
                  _val24 = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
                  _elem15[_key23] = _val24
              iprot.readMapEnd()
              self.response.append(_elem15)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()
    self.checkRequired()

  def checkRequired(self):
    return

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('ExtensionResponse')
    if self.status != None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.response != None:
      oprot.writeFieldBegin('response', TType.LIST, 2)
      oprot.writeListBegin(TType.MAP, len(self.response))
      for iter25 in self.response:
        oprot.writeMapBegin(TType.STRING, TType.STRING, len(iter25))
        for kiter26,viter27 in iter25.items():
          oprot.writeString(kiter26.encode('utf-8')) if UTF8STRINGS and not isinstance(kiter26, bytes) else oprot.writeString(kiter26)
          oprot.writeString(viter27.encode('utf-8')) if UTF8STRINGS and not isinstance(viter27, bytes) else oprot.writeString(viter27)
        oprot.writeMapEnd()
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    padding = ' ' * 4
    value = pprint.pformat(self.status, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    status=%s' % (value))
    value = pprint.pformat(self.response, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    response=%s' % (value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

class ExtensionException(TException):
  """
  Attributes:
   - code
   - message
   - uuid
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      self.checkRequired()
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      self.checkRequired()
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.code = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.message = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.uuid = iprot.readI64()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()
    self.checkRequired()

  def checkRequired(self):
    return

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('ExtensionException')
    if self.code != None:
      oprot.writeFieldBegin('code', TType.I32, 1)
      oprot.writeI32(self.code)
      oprot.writeFieldEnd()
    if self.message != None:
      oprot.writeFieldBegin('message', TType.STRING, 2)
      oprot.writeString(self.message.encode('utf-8')) if UTF8STRINGS and not isinstance(self.message, bytes) else oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.uuid != None:
      oprot.writeFieldBegin('uuid', TType.I64, 3)
      oprot.writeI64(self.uuid)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = []
    padding = ' ' * 4
    value = pprint.pformat(self.code, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    code=%s' % (value))
    value = pprint.pformat(self.message, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    message=%s' % (value))
    value = pprint.pformat(self.uuid, indent=0)
    value = padding.join(value.splitlines(True))
    L.append('    uuid=%s' % (value))
    if 'message' not in self.__dict__:
      message = getattr(self, 'message', None)
      if message:
        L.append('message=%r' % message)
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

all_structs.append(InternalOptionInfo)
InternalOptionInfo.thrift_spec = (
  None, # 0
  (1, TType.STRING, 'value', True, None, 2, ), # 1
  (2, TType.STRING, 'default_value', True, None, 2, ), # 2
  (3, TType.STRING, 'type', True, None, 2, ), # 3
)

InternalOptionInfo.thrift_struct_annotations = {
}
InternalOptionInfo.thrift_field_annotations = {
}

def InternalOptionInfo__init__(self, value=None, default_value=None, type=None,):
  self.value = value
  self.default_value = default_value
  self.type = type

InternalOptionInfo.__init__ = InternalOptionInfo__init__

all_structs.append(InternalExtensionInfo)
InternalExtensionInfo.thrift_spec = (
  None, # 0
  (1, TType.STRING, 'name', True, None, 2, ), # 1
  (2, TType.STRING, 'version', True, None, 2, ), # 2
  (3, TType.STRING, 'sdk_version', True, None, 2, ), # 3
  (4, TType.STRING, 'min_sdk_version', True, None, 2, ), # 4
)

InternalExtensionInfo.thrift_struct_annotations = {
}
InternalExtensionInfo.thrift_field_annotations = {
}

def InternalExtensionInfo__init__(self, name=None, version=None, sdk_version=None, min_sdk_version=None,):
  self.name = name
  self.version = version
  self.sdk_version = sdk_version
  self.min_sdk_version = min_sdk_version

InternalExtensionInfo.__init__ = InternalExtensionInfo__init__

all_structs.append(ExtensionStatus)
ExtensionStatus.thrift_spec = (
  None, # 0
  (1, TType.I32, 'code', None, None, 2, ), # 1
  (2, TType.STRING, 'message', True, None, 2, ), # 2
  (3, TType.I64, 'uuid', None, None, 2, ), # 3
)

ExtensionStatus.thrift_struct_annotations = {
}
ExtensionStatus.thrift_field_annotations = {
}

def ExtensionStatus__init__(self, code=None, message=None, uuid=None,):
  self.code = code
  self.message = message
  self.uuid = uuid

ExtensionStatus.__init__ = ExtensionStatus__init__

all_structs.append(ExtensionResponse)
ExtensionResponse.thrift_spec = (
  None, # 0
  (1, TType.STRUCT, 'status', [ExtensionStatus, ExtensionStatus.thrift_spec, False], None, 2, ), # 1
  (2, TType.LIST, 'response', (TType.MAP,(TType.STRING,True,TType.STRING,True)), None, 2, ), # 2
)

ExtensionResponse.thrift_struct_annotations = {
}
ExtensionResponse.thrift_field_annotations = {
}

def ExtensionResponse__init__(self, status=None, response=None,):
  self.status = status
  self.response = response

ExtensionResponse.__init__ = ExtensionResponse__init__

all_structs.append(ExtensionException)
ExtensionException.thrift_spec = (
  None, # 0
  (1, TType.I32, 'code', None, None, 2, ), # 1
  (2, TType.STRING, 'message', True, None, 2, ), # 2
  (3, TType.I64, 'uuid', None, None, 2, ), # 3
)

ExtensionException.thrift_struct_annotations = {
}
ExtensionException.thrift_field_annotations = {
}

def ExtensionException__init__(self, code=None, message=None, uuid=None,):
  self.code = code
  self.message = message
  self.uuid = uuid

ExtensionException.__init__ = ExtensionException__init__

fix_spec(all_structs)
del all_structs