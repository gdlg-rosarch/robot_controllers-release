Name:           ros-indigo-robot-controllers-msgs
Version:        0.5.0
Release:        0%{?dist}
Summary:        ROS robot_controllers_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
Messages for use with robot_controllers framework.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Feb 21 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.0-0
- Autogenerated by Bloom

* Sat Dec 05 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.3-1
- Autogenerated by Bloom

* Thu Oct 22 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.2-0
- Autogenerated by Bloom

* Fri Jun 12 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.1-0
- Autogenerated by Bloom

* Sat May 23 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.0-0
- Autogenerated by Bloom

* Sat Mar 28 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.3.1-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.3.0-0
- Autogenerated by Bloom

* Fri Mar 13 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.1.4-0
- Autogenerated by Bloom

