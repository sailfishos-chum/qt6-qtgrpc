%global qt_version 6.8.3


Summary: Qt6 - Support for using gRPC and Protobuf
Name:    qt6-qtgrpc
Version: 6.8.3
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io

Source0: %{name}-%{version}.tar.bz2

# filter plugin provides
%global __provides_exclude_from ^%{_qt6_plugindir}/.*\\.so$

BuildRequires: qt6-rpm-macros

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtdeclarative-devel >= %{qt_version}
#BuildRequires: pkgconfig(grpc++)
#BuildRequires: pkgconfig(libprotobuf-c)
BuildRequires: pkgconfig(protobuf)
BuildRequires: zlib-static

BuildRequires: protobuf-lite
BuildRequires: protobuf-compiler

BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
Protocol Buffers (Protobuf) is a cross-platform data format used to
serialize structured data. gRPC provides a remote procedure call
framework based on Protobuf. Qt provides tooling and classes to
use these technologies.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: pkgconfig(grpc++)
Requires: pkgconfig(protobuf)
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=OFF \
  -DQT_INSTALL_EXAMPLES_SOURCES=OFF \
  %{nil}

cat config.summary ||:

%cmake_build


%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/GPL* LICENSES/LGPL*
#%%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Grpc.so.6*
%{_qt6_libdir}/libQt6Protobuf.so.6*
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.so.6*
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.so.6*
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.so.6*
%{_qt6_libdir}/libQt6GrpcQuick.so.6*
%{_qt6_libdir}/libQt6ProtobufQuick.so.6*
%{_qt6_archdatadir}/qml/QtGrpc
%{_qt6_archdatadir}/qml/QtProtobuf

%files devel
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_headerdir}/QtGrpc/
%{_qt6_headerdir}/QtProtobuf/
%{_qt6_headerdir}/QtProtobufQtCoreTypes/
%{_qt6_headerdir}/QtProtobufQtGuiTypes/
%{_qt6_headerdir}/QtProtobufWellKnownTypes/
%{_qt6_headerdir}/QtGrpcQuick
%{_qt6_headerdir}/QtProtobufQuick
%{_qt6_libdir}/libQt6Grpc.so
%{_qt6_libdir}/libQt6Protobuf.so
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.so
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.so
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.so
%{_qt6_libdir}/libQt6Grpc.prl
%{_qt6_libdir}/libQt6Protobuf.prl
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.prl
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.prl
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.prl
%{_qt6_libdir}/libQt6GrpcQuick.so
%{_qt6_libdir}/libQt6GrpcQuick.prl
%{_qt6_libdir}/libQt6ProtobufQuick.so
%{_qt6_libdir}/libQt6ProtobufQuick.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtGrpcTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6GrpcTools/
%{_qt6_libdir}/cmake/Qt6GrpcTools/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Grpc/
%{_qt6_libdir}/cmake/Qt6Grpc/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Protobuf/
%{_qt6_libdir}/cmake/Qt6Protobuf/*.cmake*
%dir %{_qt6_libdir}/cmake/Qt6ProtobufQtCoreTypes/
%{_qt6_libdir}/cmake/Qt6ProtobufQtCoreTypes/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ProtobufQtGuiTypes/
%{_qt6_libdir}/cmake/Qt6ProtobufQtGuiTypes/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ProtobufTools/
%{_qt6_libdir}/cmake/Qt6ProtobufTools/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ProtobufWellKnownTypes/
%{_qt6_libdir}/cmake/Qt6ProtobufWellKnownTypes/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6GrpcQuick
%{_qt6_libdir}/cmake/Qt6GrpcQuick/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ProtobufQuick
%{_qt6_libdir}/cmake/Qt6ProtobufQuick/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc
%{_qt6_libexecdir}/qtgrpcgen
%{_qt6_libexecdir}/qtprotobufgen
