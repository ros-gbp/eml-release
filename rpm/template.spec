Name:           ros-kinetic-eml
Version:        1.8.15
Release:        3%{?dist}
Summary:        ROS eml package

Group:          Development/Libraries
License:        Binary Only
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-catkin
BuildRequires:  cmake

%description
This is an implementation of the EtherCAT master protocol for the PR2 robot
based on the work done at Flanders' Mechatronics Technology Centre.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Apr 02 2018 David Feil-Seifer <dave@cse.unr.edu> - 1.8.15-3
- Autogenerated by Bloom

* Mon Apr 02 2018 David Feil-Seifer <dave@cse.unr.edu> - 1.8.15-2
- Autogenerated by Bloom

* Mon Apr 02 2018 David Feil-Seifer <dave@cse.unr.edu> - 1.8.15-1
- Autogenerated by Bloom

