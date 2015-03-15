Lantern - Analysing Backlight on Linux
======================================

The goal of the project is to improve the understanding and awareness of the
situation of screen backlight support on Linux. Currently the project is in
nascent state, collecting submissions created by lantern-collect and storing
them directly in this repository.

TODO
====

If you are interested in contributing you can start by following this list, any
idea is good though, just open issues, talk to us on IRC (``#checkbox`` on
freenode) or send emails to Zygmunt Krynicki
zygmunt<dot>krynicki<at>canonical.com

- Run ./lantern-collect and send me the resulting tarball
- Contribute answers to the questions listed below:
- Improve any of the data-analysis scripts in this repository (statistics,
  graphs!)
- Create a plainbox provider that can perform the interactive tests
- Design open source hardware that can measure screen brightness
- Interface with existing measurement hardware

Open Questions
==============

Basics
------

- What are the values of ``/sys/class/backlight/*/max_brightness`` as seen in
  the wild?
- What is the usage ratio of each of the three possible values of
  ``/sys/class/backlight/*/type`` (``raw``, ``firmware``, ``platform``)?
- When ``/sys/class/*/actual_brightness`` is zero is the backlight off or just
  very dim?
- Do ``/sys/class/*/{actual_,}brightness`` agree when using hardware brightness
  control keys?
- Do ``/sys/class/*/{actual_,}brightness`` change when using the hardware
  brightness control keys? 
- Does the firmware remember the value set by hardware brightness control keys?
- What is the value after reboot?
- Is there a difference between what happens in X and on vt*?

With extra hardware
-------------------

- What is the plot of distinct values of ``/sys/class/backlight/*/brightness``
  against emitted light?
- Is there *off-the-shelf* hardware that can measure it?

Windows Factor
--------------

- What are the requirements of Windows hardware certification programme on the
  backlight interface?
- What does ACPI say about brightness? (this is a personal learning goal)
- Are the values reported by Windows (using standard Windows APIs) identical to
  what Linux sees?

Android Factor
--------------

- How does this work on AOSP
- How does it work in practice on available handsets?

Apple Factor
------------

- What does Apple offer as far as drivers and userspace control?
- What does Linux see when booting on Apple hardware?

Standardization
---------------

- Which relevant standards apply?

License
=======

Lantern is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License version 3,
as published by the Free Software Foundation.

Lantern is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Lantern.  If not, see <http://www.gnu.org/licenses/>.
