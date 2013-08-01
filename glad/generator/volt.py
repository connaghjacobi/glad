from glad.generator import DGenerator
import os.path


class VoltGenerator(DGenerator):
    MODULE = 'gl'
    LOADER = 'loader'
    GL = 'package'
    ENUMS = 'enums'
    EXT = 'ext'
    FUNCS = 'funcs'
    TYPES = 'types'
    FILE_EXTENSION = '.volt'
    API = ''

    LOAD_GL_NAME = 'loadGL'

    def write_module(self, fobj, name):
        if name == 'package':
            fobj.write('module {};\n\n'.format(self.MODULE))
        else:
            DGenerator.write_module(self, fobj, name)

    def write_extern(self, fobj):
        fobj.write('extern(System) @loadDynamic:\n')

    def write_extern_end(self, fobj):
        pass

    def write_shared(self, fobj):
        pass

    def write_shared_end(self, fobj):
        pass

    def write_func(self, fobj, func):
        pass

    def write_func_prototype(self, fobj, func):
        fobj.write('{} {}('
                .format(func.proto.ret.to_volt(), func.proto.name))
        fobj.write(', '.join(param.type.to_volt() for param in func.params))
        fobj.write(');\n')

    def write_boolean(self, fobj, name):
        fobj.write('global bool {};\n'.format(name))

    def write_enum(self, fobj, name, value, type='uint'):
        if value.startswith('0x') and type.startswith('u'):
            value += 'U'
        if len(value) > 12 and type.startswith('u'):
            value += 'L'

        try:
            v = int(value)
            if v < 0:
                type = 'int'
        except ValueError:
            pass

        fobj.write('enum {} {} = {};\n'.format(type, name, value))
