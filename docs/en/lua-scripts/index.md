# **Lua** **Scripts**

Lua scripts allow you to create custom widgets to display information in the Ethos main views. In future it will also allow you to modify the behavior of the radio to add specialized functions for custom tasks, and to interface with flight controllers and the like.

The Lua scripting language is a lightweight embeddable scripting language and is designed to be used for all sorts of applications from games to web applications and image processing, and in this case for implementing custom functions in the radio.

Please note that Lua scripts increase the startup time of the radio. If they are implemented correctly the delay should not be noticeable, but if it is not the case, then the delay may be almost indefinite.
