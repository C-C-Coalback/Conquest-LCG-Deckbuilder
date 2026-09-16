def get_light_mode(request):
    try:
        value = request.COOKIES.get('light_mode')
        if value is None:
            return "Light"
        return value
    except Exception as e:
        print(e)
    return "Light"
