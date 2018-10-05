from QueryBuilder import QueryBuilder as Qb
from SbxPy import SbxCore as Sc
import asyncio
import os

'''
This is a test using the os environment:
credentials app: APP-KEY, DOMAIN
credentials user: LOGIN, PASSWORD
'''

async def main(sci):

    qb = Qb()
    qb.set_domain(123)
    qb.add_object({'user': 'data'})
    print(qb.compile())

    qb = Qb()
    qb.set_domain(123)
    qb.add_condition('AND', 'name', '=', 'pepe')
    qb.add_condition('AND', 'edad', '>', 50)
    qb.new_group('OR')
    qb.add_condition('AND', 'genero', '=', 'M')
    print(qb.compile())

    login = await  sci.login(os.environ['LOGIN'], os.environ['PASSWORD'], os.environ['DOMAIN'])
    print(login)


sc = Sc(manage_loop=True)
sc.initialize(os.environ['DOMAIN'], os.environ['APP-KEY'], os.environ['SERVER_URL'])
loop = asyncio.new_event_loop()

data = loop.run_until_complete(main(sc))


def callback(error, result):
    if error is not None:
        print(error)
    else:
        print(result)
    sc.close_connection()


sc.loginCallback(os.environ['LOGIN'], os.environ['PASSWORD'], os.environ['DOMAIN'],callback)
