import argparse


class ArgumentsReader:

    def __init__(self):
        parser = argparse.ArgumentParser()

        # General arguments
        parser.add_argument("--host-platform", "-hp", type=str, default="osx", help="computer platform. Values [osx/windows]")
        parser.add_argument("--platform", "-p", type=str, default="osx", help="test platform. Values [ios/android]")
        parser.add_argument("--auto-detect-device", "-add", type=int, help="number of device to auto detect to run tests on. Values: [1..n]")
        parser.add_argument("--device-id", "-i", type=str, help="device id to run tests on. Used when auto detection is not allowed. Value: string")
        parser.add_argument("--tests", "-t", type=str, default="TestsTreeTemplate.json", help="path to tests tree template json file. Value: string")
        parser.add_argument("--build", "-b", type=str, help="path to .apk for android / .ipa or .app for iOS. Value: string")
        parser.add_argument("--bundle", "-app", type=str, help="application bundle. Value: string")
        parser.add_argument("--port-local", "-pl", type=str, default="13000", help="local machine port to set up port forwarding. Values [13000, 13001, 13002,...n]")
        parser.add_argument("--port-device", "-pd", type=str, default="13000", help="connected device port to set up port forwarding. Values [13000, 13001, 13002,...n]")

        # Skipping some run steps
        parser.add_argument("--skip-port-forward", "-sp", type=bool, action=argparse.BooleanOptionalAction, help="skip port forwarding. Values [true/false]")
        parser.add_argument("--skip-server-run", "-ss", type=bool, action=argparse.BooleanOptionalAction, help="skip running (or opening if it's already ran) application on device. Values [true/false]")
        parser.add_argument("--skip-session-run", "-sr", type=bool, action=argparse.BooleanOptionalAction, help="skip installing and running application with initialization of appium session. Warning: tests that use appium API will not run. Values [true/false]")
        parser.add_argument("--skip-tests", "-st", type=bool, action=argparse.BooleanOptionalAction, help="skip running tests. Values [true/false]")

        # Android specific arguments
        parser.add_argument("--adb", type=str, help="adb path. Value: string")
        parser.add_argument("--android-home", type=str, help="android SDK directory path. Value: string")
        parser.add_argument("--java-home", type=str, help="java home path. Value: string")

        # iOS specific arguments
        parser.add_argument("--team-id", type=str, default="J86B8Y8A5P", help="team id. Value: string")
        parser.add_argument("--signing-id", type=str, default="Apple Development", help="signing id. Value: string")

        self._parser = parser
        self._arguments = parser.parse_args()

    @property
    def arguments(self):
        return self._arguments
