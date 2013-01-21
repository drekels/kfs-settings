import opt_type
from exception import InvalidOptionException, CommandImplementationError


class Option(object):

    def __init__(self, name, description, short="", otype=None, default=None,
                 mandatory=False, position=None):
        self.name = name
        self.description = description
        self.short = short
        self.lower = self.name.lower()
        self.flag = "--{}".format(self.lower.replace("_", "-"))
        self.mandatory = mandatory
        self.position = position
        if not otype:
            otype = opt_type.FLAG
        self.otype = otype
        self.default = default
        if default == None:
            self.default = self.otype.default
        self._validate_default

    def __call__(self, command, *args):
        self.otype.set_value(self, command, *args)
        value = command.getattr(self.lower)
        if not self._is_valid(value):
            raise InvalidOptionException("'{}' is an invalid value for option '{}', {}".format(value, self.flag,
                                         self.error_string(value)))

    def is_valid(self, value):
        """ Defaults to only validate the option type """
        return True

    def error_string(self, value):
        return self.otype.error_string(value)

    def _is_valid(self, value):
        return self.otype.is_valid(value) and self.is_valid(value)

    def _validate_default(self):
        if not self._is_valid(self.default):
            raise CommandImplementationError("'{}' is an invalid default value for option '{}', {}".format(
                                             self.default, self.name, self.error_string(self.default)))


class HelpOption(Option):
    def __init__(self):
        Option.__init__(self, "HELP", "Displays this message", short="-h", otype=opt_type.FLAG)
