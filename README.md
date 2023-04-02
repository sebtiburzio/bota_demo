# Getting started using Bota FT sensors with FR3 arms

- Firstly, you will need the [BOTA driver](https://gitlab.com/botasys/bota_driver). Install it and read the instructions for the driver, as well as the Bota Demo repo instructions (below)
- Modifications to the franka_ros package are also required, see [here](https://github.com/sebtiburzio/franka_ros.git)
- This repo contains slightly modified launch files (with '_fr3' added to the file names) which will set up the driver to measure the wrist wrench for an FR3 arm
- 'Fake' gravity compensation is done using the orientation of the robot wrist link. The mass/COM properties used for compensation are stored in `config/gravity_comp_*.yaml`. Calibration has been done for the empty sensor and the Franka Hand, using the procedure from the `force_torque_tools` package, see [here](https://github.com/sebtiburzio/force_torque_tools.git). You can use that package to calibrate a different gripper (change loaded config [here](https://github.com/sebtiburzio/bota_demo/blob/bc8981895af2fb803224e503d5fd2072dca7bbd9/launch/bota_fr3.launch#L14))
- The static bias in the configs has not been set, as it is recommended to set this manually after launching the sensor/robot using the `ResetWrench` action (orient the sensor vertically and set all to zero except the known gripper weight in Z axis).

The rest of the instructions below are from the upstream Bota Demo repo.

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

Run the launch file which is related with your product, you can find your product name on the product label.

#### Serial

The `roslaunch` commands with only serial devices works without `root` privileges provided that the user is in the `dialout` group. This can be done with:

```bash
sudo usermod -a -G dialout username
```
Please log off and log in again for the changes to take effect!

To run the sensor you can use the following command as an example:
```bash
roslaunch bota_demo BFT_ROKA_SER_M8.launch
```

#### EtherCAT

The EtherCAT device driver is using SOEM which requires access to certain network capabilities as it is using raw sockets, and as such any executable linking against SOEM needs to be run with certain privileges.
Typically, you would run any SOEM executables with `sudo` or as `root`. This is impractical for any ROS system, and as such there exists a tool called [`ethercat_grant`](https://github.com/shadow-robot/ethercat_grant) that helps with that.

If you followed the installation instructions for the [`bota_driver`](https://gitlab.com/botasys/bota_driver), `ethercat_grant` is already installed. Alternatively, you can install it with
```bash
sudo apt install ros-<DISTRO>-ethercat-grant
```
and add the following `launch prefix` to the `node` tag of the `rokubimini_ethercat_bus_manager_node` in your launch file:
```xml
launch-prefix="ethercat_grant"
```
**Note:** This launch prefix is already added to all the launch files in this repo.

To run the sensor you can use the following command as an example:
```bash
roslaunch bota_demo BFT_ROKA_ECAT_M8.launch
```
For more complicated examples have a look at `BFT_SENS_ECAT_M8_realsense.launch` to see how to combine our sensor with a realsense camera.

##### (Alternative:) EtherCAT without launch prefix

Instead of using the `ethercat_grant` launch prefix, the above command to interface with your EtherCAT sensor can also be combined with escalated privileges (e.g. `su root` or `sudo su`, if you don't have set a `root` password).


## Support

For any queries or problems found with the software provided, please contact us at `sw-support@botasys.com`
