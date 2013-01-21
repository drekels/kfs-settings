import option
import opt_type
from exception import InvalidOptionException
import sys
from StringIO import StringIO
import traceback


PARAM_MAP = {opt_type.NO_PARAMS: "_get_flag_params",
             opt_type.ONE_PARAM: "_get_one_param",
             opt_type.N_PARAMS: "_get_n_params",
            }


class Command(object):
    _default_options = [option.HelpOption()]
    example = None

    def __init__(self, called_command=None):
        self._optmap = {}
        self._positions = []
        self._mandatory = set([])
        self._options_used = set([])
        self.called_command = called_command

    def __call__(self, *args):
        if self.called_command:
            try:
                self._call(*args)
            except InvalidOptionException as e:
                    sys.stderr.write("Command Failed: {}\n".format(e.message))
                    print self.get_help()
        else:
            self._call(*args)

    def call(self, *args):
        self(*args)

    def get_help(self):
        helpstr = StringIO()
        helpstr.write("Usage: {} [OPTION]...\n".format(self.called_command))
        helpstr.write("{}\n".format(self.describe()))
        if self.example:
            helpstr.write("{}\n".format(self.example))
        helpstr.write("\nOptions:\n")
        maxflag = max([len(option.flag) for option in self.options])
        for option in self.options:
            helpstr.write("  {} {:<{maxflag}} {}\n".format(option.short, option.flag, option.description,
                          maxflag=maxflag))
        return helpstr.getvalue()

    def run(self):
        raise NotImplementedError()

    def describe(self):
        raise NotImplementedError()

    def config_env(self):
        raise NotImplementedError()

    def _call(self, *args):
        self.options.extend(self._default_options)
        self._compile_options()
        self._process_arguments(args)
        if not self._mandatory.issubset(self._options_used):
            error = "The following mandatory options are missing:\n"
            for option in self._mandatory - self._options_used:
                error += "    {}\n".format(option.flag)
            raise InvalidOptionException(error)
        self.run()

    def _compile_options(self):
        for option in self.options:
            self._optmap[option.short] = option
            self._optmap[option.flag] = option
            setattr(self, option.lower, option.default)
            self._set_position(option)
            if option.mandatory:
                self._mandatory.add(option)

    def _process_arguments(self, args):
        if not args:
            return
        arglist = [arg for arg in args]
        arg = arglist.pop(0)
        option = None
        if arg in self._optmap:
            option = self._optmap[arg]
        else:
            try:
                option = self._positions.pop(0)
            except KeyError:
                _raise_unknown_option(arg)
        self._options_used.add(option)
        arglist = option.otype.set_value(self, option, arglist)
        self._process_arguments(arglist)

    def _set_position(self, option):
        if not option.position:
            return
        if isinstance(option.position, int):
            while len(self._positions) <= option.position:
                self._positions.append("_")
            self._positions[option.position] = option
        else:
            try:
                self._positions[self._positions.index("_")] = option
            except ValueError:
                self._positions.append(option)

def _raise_unknown_option(option):
    raise InvalidOptionException("Unknown option '{}'".format(option))
