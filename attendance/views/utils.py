def format_form_errors(errors):
    error_list = []
    for field, field_errors in errors.items():
        for error in field_errors:
            error_list.append(f"{field.capitalize()}: {error}")
    return error_list
