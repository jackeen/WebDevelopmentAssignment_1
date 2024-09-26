def format_form_errors(errors):
    error_list = []
    for field, field_errors in errors.items():
        for error in field_errors:
            field_name = field.capitalize()
            if field_name == '__all__':
                field_name = ''
            else:
                field_name += ': '
            error_list.append(f"{field_name}{error}")
    return error_list
