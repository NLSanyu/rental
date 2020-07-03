from rental.apps.core.renderers import RentalJSONRenderer

class UserJSONRenderer(RentalJSONRenderer):
    object_label = 'user'

    def render(self, data, media_type=None, renderer_context=None):
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        # Render user data under the "user" namespace
        return super(UserJSONRenderer, self).render(data)
