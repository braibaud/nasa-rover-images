
import asyncio
import argparse
from enum import Enum
import rover_perseverance as rp
import rover_curiosity as rc

class Rover(Enum):
    perseverance = 'perseverance'
    curiosity = 'curiosity'

    def __str__(self):
        return self.value


# parse command-line arguments
parser = argparse.ArgumentParser(
    description='NASA raw images downloader')

parser.add_argument(
    '-c',
    '--cache_location',
    default=None,
    type=str,
    help='Location of the cache folder base.')

parser.add_argument(
    '-r', 
    '--rover_name', 
    type=Rover,
    choices=list(Rover),
    default=Rover.perseverance,
    help='Name of the rover')

parser.add_argument(
    '-t', 
    '--thumbnail', 
    action='store_true',
    help='Set to download thumbnail images also')

parser.add_argument(
    '-i', 
    '--incremental', 
    action='store_true',
    help='Incremental updates only')

FLAGS = parser.parse_args()


# Program entrance
if __name__ == '__main__':

    rover = None

    # check which rover we're talking about
    if FLAGS.rover_name == Rover.perseverance:
        rover = rp.PerseveranceConfig(FLAGS)
    elif FLAGS.rover_name == Rover.curiosity:
        rover = rc.CuriosityConfig(FLAGS)

    print('Rover:       {0}'.format(FLAGS.rover_name))
    print('Cache:       {0}'.format(FLAGS.cache_location))
    print('Thumbnails:  {0}'.format(FLAGS.thumbnail))
    print('Incremental: {0}'.format(FLAGS.incremental))

    if rover is not None:
        asyncio.run(
            main=rover.run(FLAGS.incremental))
