from config import *
import sys

if __name__=="__main__":
    rabit=RabitMQConnection()
    try:
        rabit.consume_task()
    except KeyboardInterrupt:
        sys.exit(0)
            