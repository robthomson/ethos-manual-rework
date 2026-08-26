# Command line operation

FrSky Suite can be run from a terminal command line.

The following command line options are available:

| --help | help text for the FrSky Suite command line tool. |
| --- | --- |
| --version | show the version of the installed FrSky Suite. |
| --list-radios | list all the supported FrSky radios. |
| --radio-components<br>--radio {RADIO}<br>--radio auto | list all the components and their paths. <br>If multiple radios are connected to your computer, you can use \[--radio {RADIO}\] to specify one. <br>Otherwise, you can omit \[--radio {RADIO}\] or use  \[--radio auto\] for automatic detection. |
| --get-path {COMPONENT} | get the path of the given component. <br>Currently supported components: BITMAPS, SCRIPTS, SCREENSHOTS, AUDIO, I18N. |
| --serial start\|stop | enable / disable the serial debug mode. |

Notice: The Suite app will not start unless it successfully recognizes a command.
