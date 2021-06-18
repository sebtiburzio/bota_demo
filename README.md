# BOTA Demo - README

## Overview

This software package provides a demo with examples for running the [BOTA driver](https://gitlab.com/botasys/bota_driver).

**Author(s):** Lefteris Kotsonis, Ilias Patsiaouras, Mike Karamousadakis


## Installation

### Cloning the package

Clone the package with:

```bash
git clone https://gitlab.com/botasys/bota_demo.git
```

### Building from Source

In order to use the `bota_demo` package, you need to clone/download the following source dependencies:

#### Source Dependencies

- [force_torque_tools](https://github.com/kth-ros-pkg/force_torque_tools/tree/kinetic)

After cloning the package and before building, you need also to make sure that all the binary dependencies are installed. To do so, run in a terminal:

```bash
cd catkin_workspace/ && rosdep update && rosdep install --from-path src --ignore-src -y
```

#### Building

Compile the package using the `catkin_tools` package:
   
```bash
cd catkin_workspace
catkin build bota_demo
```

## Usage

### Launching

Run the launch file which is related with your product, you can find your product name on the product label. Be careful and use root privileges if you are using an EtherCAT device (for Serial it's not necessary if you have included your user to the `dialout` group):

```bash
    roslaunch bota_demo BFT_ROKA_ECAT_M8.launch
    # OR
    roslaunch bota_demo BFT_ROKA_SER_M8.launch
```

For more complicated examples have a look at BFT_SENS_ECAT_M8_realsense.launch to see how to combine our sensor with a realsense camera

## Support

For any queries or problems found with the software provided, please contact us at `sw-support@botasys.com`
