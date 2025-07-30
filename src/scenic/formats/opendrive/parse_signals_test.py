import sys

from scenic.formats.opendrive import xodr_parser

def main(path):
    road_map = xodr_parser.RoadMap() #Create an instance of the RoadMap class. Empty for now
    road_map.parse(path) #Parse the .xodr file and extract things like roads, lanes, crosswalks, etc.
    total_signals = 0

    for road_id, road in road_map.roads.items(): #Loop through every road 
        if road.signals: 
            print(f"Road {road_id} has {len(road.signals)} signals(s)")

            for signal in road.signals: #road.crosswalks gets appended to in xodr_parser
                print(f"id: {signal.id_}")
                print(f"country: {signal.country}")
                print(f"type: {signal.type_}")
                print(f"subtype: {signal.subtype}")
                print(f"orientation: {signal.orientation}")
                print(f"validity: {signal.validity}")


                print(f"s: {signal.s:.2f}")
                print(f"t: {signal.t:.2f}")
                print(f"zOffset: {signal.zOffset:.2f}")
                print(f"hOffset: {signal.hOffset:.2f}")

                print(f"height: {signal.height:.2f}")
                print(f"width: {signal.width:.2f}")

                print()

            total_signals += len(road.signals)

    print("Total signals:", total_signals)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid Usage: python parse_signals_test.py path_to_file.xodr")
    else:
        main(sys.argv[1])