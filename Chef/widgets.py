from django.forms import forms, widgets
from django.forms import DateInput, TimeInput, MultiWidget


class DateWidget(DateInput):
    """
    DateWidget is the corresponding widget for Date field, it renders only the date section of
    datetime picker.
    """

    format_name = 'DATE_INPUT_FORMATS'
    glyphicon = 'glyphicon-calendar'

    def __init__(self, attrs=None, options=None):

        if options is None:
            options = {}

        # Set the default options to show only the datepicker object
        options['startView'] = options.get('startView', 2)
        options['minView'] = options.get('minView', 2)
        options['format'] = options.get('format', 'dd/mm/yyyy')

        super(DateWidget, self).__init__(attrs, options)


class TimeWidget(TimeInput):
    """
    TimeWidget is the corresponding widget for Time field, it renders only the time section of
    datetime picker.
    """

    format_name = 'TIME_INPUT_FORMATS'
    glyphicon = 'glyphicon-time'

    def __init__(self, attrs=None, options=None):

        if options is None:
            options = {}

        # Set the default options to show only the timepicker object
        options['startView'] = options.get('startView', 1)
        options['minView'] = options.get('minView', 0)
        options['maxView'] = options.get('maxView', 1)
        options['format'] = options.get('format', 'hh:ii')

        super(TimeWidget, self).__init__(attrs, options)



