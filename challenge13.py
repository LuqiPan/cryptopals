import random
import re

def decode_url_params(url_params):
    return {component.split('=')[0]:component.split('=')[1] for component in url_params.split('&')}

def encode_url_params(params):
    return '&'.join([str(k) + '=' + str(v) for k, v in params.iteritems()])

def profile_for(email):
    email = re.sub(r'&|=', '', email)
    return encode_url_params(
        {
            'email': email,
            'uid': random.randint(0,100),
            'role': 'admin' if random.randint(0,2) == 0 else 'user'
        }
    )

# TODO: missing 2 functions for encrypt and decrypt user profile

if __name__ == '__main__':
    url_params = 'foo=bar&baz=qux&zap=zazzle'
    print decode_url_params(url_params)
    print profile_for('foo@bar.com&role=admin')
    print decode_url_params(profile_for('foo@bar.com&role=admin'))
