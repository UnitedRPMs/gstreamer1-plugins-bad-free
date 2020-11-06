%global         majorminor 1.0
%global         _gobject_introspection  1.31.1

%global debug_package %{nil}

%bcond_with libfdk-aac
# We need to test it
#Please read here https://bugzilla.redhat.com/show_bug.cgi?id=1501522

# Only have extras package on fedora
%if 0%{?fedora}
%bcond_without extras
%else
%bcond_with extras
%endif

%define _legacy_common_support 1


Name:           gstreamer1-plugins-bad-free
Version:        1.18.1
Release:        8%{?dist}
Summary:        GStreamer streaming media framework "bad" plugins

License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
Source1:        gst-p-bad-cleanup.sh

# https://gitlab.freedesktop.org/gstreamer/common/-/merge_requests/4
# https://bugzilla.redhat.com/show_bug.cgi?id=1799497
Patch0:         gstreamer1-plugins-bad-build-adapt-to-backwards-incompatible-change.patch
 
# https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/-/merge_requests/1125
# https://bugzilla.redhat.com/show_bug.cgi?id=1799497
Patch1:         gstreamer1-plugins-bad-lv2-make-it-build-with-fno-common.patch

Patch2:	gst-plugins-bad-1.16.2-make43.patch


BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gobject-introspection-devel >= %{_gobject_introspection}

BuildRequires:  bzip2-devel
BuildRequires:  exempi-devel
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
BuildRequires:  fdk-aac-free-devel
%endif
BuildRequires:  gsm-devel
BuildRequires:  jasper-devel
BuildRequires:  ladspa-devel
BuildRequires:  lcms2-devel
BuildRequires:  libdvdnav-devel
BuildRequires:  libexif-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libnice-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsndfile-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openssl-devel
BuildRequires:  orc-devel
BuildRequires:  soundtouch-devel
BuildRequires:  wavpack-devel
BuildRequires:  opus-devel
BuildRequires:  nettle-devel
BuildRequires:  libgcrypt-devel
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  wayland-devel
%endif
BuildRequires:  gnutls-devel
BuildRequires:  libsrtp-devel
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  gtk3-devel >= 3.4
BuildRequires:  bluez-libs-devel >= 5.0
BuildRequires:  libwebp-devel
#BuildRequires:  mesa-libEGL-devel
BuildRequires:  vulkan-devel
#BuildRequires:  mesa-vulkan-devel
BuildRequires:  webrtc-audio-processing-devel
BuildRequires:  libaom-devel
BuildRequires:  libmicrodns-devel
%if 0%{?fedora} >= 31
BuildRequires:  libopenmpt-devel
BuildRequires:  pkgconfig(libva-drm)
%endif
BuildRequires:  srt-devel
%if 0
BuildRequires:  wpewebkit-devel
BuildRequires:  wpebackend-fdo-devel
%endif
BuildRequires:  glslc
BuildRequires:  libdrm-devel
BuildRequires:  liblrdf-devel
BuildRequires:  zvbi-devel

%if %{with extras}
BuildRequires:  libbs2b-devel >= 3.1.0
## Plugins not ported
#BuildRequires:  dirac-devel
#BuildRequires:  gmyth-devel >= 0.4
BuildRequires:  fluidsynth-devel
BuildRequires:  libass-devel
BuildRequires:  libchromaprint-devel
## Plugin not ported
#BuildRequires:  libcdaudio-devel
BuildRequires:  libcurl-devel
BuildRequires:  libssh2-devel
BuildRequires:  libxml2-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  libkate-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libofa-devel
## Plugins not ported
#BuildRequires:  libmusicbrainz-devel
#BuildRequires:  libtimidity-devel
BuildRequires:  libvdpau-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  mesa-libGLES-devel
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  libXext-devel
BuildRequires:  openal-soft-devel
BuildRequires:  opencv-devel >= 4.5.0
BuildRequires:  openjpeg2-devel
BuildRequires:  pkgconfig(spandsp) >= 0.0.6
## Plugins not ported
#BuildRequires:  SDL-devel
BuildRequires:  lilv-devel
BuildRequires:  wildmidi-devel
BuildRequires:  zbar-devel
BuildRequires:  OpenEXR-devel
%endif

# libgstfdkaac.so used to be shipped in -nonfree
Obsoletes: gstreamer1-plugins-bad-nonfree < 1.16.1-2

BuildRequires:  gtk-doc
BuildRequires:	chrpath
BuildRequires:	make tar xz
# For libfdk-aac
%if %{without libfdk-aac}
BuildRequires: fdk-aac-free-devel
%endif

# For aom (av1)
%if 0%{?fedora} >= 33
BuildRequires:  libaom-devel >= 2.0.0
%else
BuildRequires:  libaom-devel
%endif 

# New
BuildRequires: meson
BuildRequires: cmake
BuildRequires: libltc-devel
BuildRequires: game-music-emu-devel

# Drop after f36
Provides: gst-transcoder = 1.16.0-4
Obsoletes: gst-transcoder < 1.16.0-4

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested well enough, or the code
is not of good enough quality.

%package gtk
Summary:         GStreamer "bad" plugins gtk plugin
Requires:        %{name} = %{version}-%{release}
%ifarch x86_64
Provides:	 gstreamer1(element-gtksink)()(64bit)
%endif

%description gtk
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package contains the gtksink/gtk output plugin.


%if %{with extras}
%package extras
Summary:         Extra GStreamer "bad" plugins (less often used "bad" plugins)
Requires:        %{name} = %{version}-%{release}


%description extras
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package contains
extra "bad" plugins for sources (mythtv), sinks (fbdev) and
effects (pitch) which are not used very much and require additional
libraries to be installed.

%package zbar	
Summary:         GStreamer "bad" plugins zbar plugin	
Requires:        %{name}%{?_isa} = %{version}-%{release}
		
%description zbar
GStreamer is a streaming media framework, based on graphs of elements which	
operate on media data.
gstreamer-plugins-bad contains plug-ins that aren't tested well enough,	
or the code is not of good enough quality.
This package (%{name}-zbar) contains the zbar
plugin which allows decode bar codes.

%package fluidsynth
Summary:         GStreamer "bad" plugins fluidsynth plugin
Requires:        %{name} = %{version}-%{release}
Requires:        soundfont2-default

%description fluidsynth
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package contains the fluidsynth
plugin which allows playback of midi files.


%package wildmidi
Summary:         GStreamer "bad" plugins wildmidi plugin
Requires:        %{name} = %{version}-%{release}

%description wildmidi
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package contains the wildmidi
plugin which allows playback of midi files.
%endif


%package devel
Summary:        Development files for the GStreamer media framework "bad" plug-ins
Requires:       %{name} = %{version}-%{release}
Requires:       gstreamer1-plugins-base-devel


%description devel
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development files for the plug-ins that
aren't tested well enough, or the code is not of good enough quality.


%prep
# Process a gst-plugins-bad tarball to remove
# unwanted GStreamer plugins.
%{S:1} %{S:0}
%setup -T -D -n gst-plugins-bad-%{version}

# wtf?
sed -i 's|4.5.0|4.5.1|g' ext/opencv/meson.build


%build
#CFLAGS+=' -fcommon'

%meson \
    -D package-name="Fedora GStreamer-plugins-bad package" \
    -D package-origin="http://download.fedoraproject.org" \
    -D doc=disabled -D magicleap=disabled -D msdk=disabled \
    -D dts=disabled -D faac=disabled -D faad=disabled \
    -D libmms=disabled -D mpeg2enc=disabled -D mplex=disabled \
    -D neon=disabled -D rtmp=disabled -D rtmp2=disabled \
    -D flite=disabled -D sbc=disabled -D opencv=enabled \
    -D voamrwbenc=disabled -D x265=disabled \
    -D dvbsuboverlay=disabled -D dvdspu=disabled -D siren=disabled \
    -D real=disabled -D opensles=disabled -D tinyalsa=disabled \
    -D wasapi=disabled -D wasapi2=disabled -D avtp=disabled \
    -D dc1394=disabled -D directfb=disabled -D iqa=disabled \
    -D libde265=disabled -D musepack=disabled -D openni2=disabled \
    -D sctp=disabled -D svthevcenc=disabled -D voaacenc=disabled \
    -D zxing=disabled -D wpe=disabled -D x11=disabled \
    -D openh264=disabled -D srt=enabled  \
    -D lv2=enabled -D spandsp=enabled \
    -D openal=enabled -D vdpau=disabled -D uvch264=enabled \
    -D ltc=enabled -D gme=enabled \
    %if 0%{?fedora} >= 31
    -D openmpt=enabled \
    -D va=enabled \
    %else
    -D openmpt=disabled \
    -D va=disabled \
    -D examples=disabled \
    %endif

%meson_build 

%install
%meson_install 


# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/gstreamer-bad-free.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013 Richard Hughes <richard@hughsie.com> -->
<component type="codec">
  <id>gstreamer-bad-free</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>GStreamer Multimedia Codecs - Extra</name>
  <summary>Multimedia playback for AIFF, DVB, GSM, MIDI, MXF and Opus</summary>
  <description>
    <p>
      This addon includes several additional codecs that are missing
      something - perhaps a good code review, some documentation, a set of
      tests, a real live maintainer, or some actual wide use.
      However, they might be good enough to play your media files.
    </p>
    <p>
      These codecs can be used to encode and decode media files where the
      format is not patent encumbered.
    </p>
    <p>
      A codec decodes audio and video for for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <keywords>
    <keyword>AIFF</keyword>
    <keyword>DVB</keyword>
    <keyword>GSM</keyword>
    <keyword>MIDI</keyword>
    <keyword>MXF</keyword>
    <keyword>Opus</keyword>
  </keywords>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

# GStreamer gtk plugin was renamed to 'gtk' and libgstcamerabin2 to libgstcamerabin
# https://bugzilla.gnome.org/show_bug.cgi?id=779344
# https://github.com/GStreamer/gst-plugins-bad/commit/eb2dae8fd6aea04673fdd5b0fdf05e4e2ce1c2ee
ln -sf %{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so 
ln -sf %{_libdir}/gstreamer-%{majorminor}/libgstgtk.so %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstgtksink.so 

%find_lang gst-plugins-bad-%{majorminor}

# unpackaged files
if [ -f $RPM_BUILD_ROOT%{_bindir}/playout ]; then
rm $RPM_BUILD_ROOT%{_bindir}/playout
fi

find %{buildroot}/ -name '*.la' -exec rm -f {} ';'
# Kill rpath
# chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
# chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so
# chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdashdemux.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
# chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstgtksink.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
#chrpath --delete {buildroot}/{_libdir}/gstreamer-{majorminor}/libgstopengl.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
##chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstuvch264.so
##chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstvdpau.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
#chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
chrpath --delete %{buildroot}/%{_libdir}/libgstadaptivedemux-%{majorminor}.so

chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstopenjpeg.so

# It is provided by gst-transcoder, we don't need it here
# but gstreamer-bad-transcoder exist now; maybe is necessary make a new sub-package
#rm -f %{buildroot}/%{_bindir}/gst-transcoder-%{majorminor}
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgsttranscode.so
#rm -f %{buildroot}/%{_libdir}/libgsttranscoder-%{majorminor}.so.*
#rm -f %{buildroot}/%{_libdir}/libgsttranscoder-%{majorminor}.so
rm -f %{buildroot}/%{_libdir}/girepository-1.0/GstTranscoder-1.0.typelib
rm -rf %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/transcoder
rm -f %{buildroot}/%{_libdir}/pkgconfig/gstreamer-transcoder-%{majorminor}.pc
rm -f %{buildroot}/%{_datadir}/gir-1.0/GstTranscoder-%{majorminor}.gir

# presets
rm -rf %{buildroot}/%{_datadir}/gstreamer-%{majorminor}/presets/
rm -rf %{buildroot}/%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/
##########

# It is provided by freeworld, we don't need it here
#rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdvbsuboverlay.so 
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so 
#rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstfdkaac.so 
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstopenh264.so
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstqmlgl.so 
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstsiren.so 
#

# It is provided by plugins-base, we don't need it here
rm -f %{buildroot}/%{_libdir}/girepository-1.0/GstGL-1.0.typelib
rm -f %{buildroot}/%{_libdir}/gstreamer-1.0/libgstaudiomixer.so
rm -f %{buildroot}/%{_libdir}/gstreamer-1.0/libgstopengl.so
rm -f %{buildroot}/%{_libdir}/libgstgl-1.0.so.0
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/base/gstaggregator.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/allocators/gstphysmemory.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstaudioaggregator.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/egl/gsteglimage.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/egl/gstgldisplay_egl.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/egl/gstglmemoryegl.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gl.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstgl_fwd.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglapi.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglbasefilter.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglbasememory.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglbuffer.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglbufferpool.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglcontext.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstgldebug.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstgldisplay.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglfilter.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglformat.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglframebuffer.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglmemorypbo.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstgloverlaycompositor.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglquery.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglrenderbuffer.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglshader.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglshaderstrings.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglsl.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglupload.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglutils.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglviewconvert.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglwindow.h
rm -f %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/gl/x11/gstgldisplay_x11.h
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/include/gst/gl/gstglconfig.h
rm -f %{buildroot}/%{_libdir}/libgstgl-%{majorminor}.so
rm -f %{buildroot}/%{_libdir}/pkgconfig/gstreamer-gl-%{majorminor}.pc
rm -f %{buildroot}/%{_datadir}/gir-%{majorminor}/GstGL-%{majorminor}.gir


%files -f gst-plugins-bad-%{majorminor}.lang
%license COPYING 
%doc AUTHORS README REQUIREMENTS

%{_bindir}/gst-transcoder-%{majorminor} 
%{_libdir}/libgsttranscoder-%{majorminor}.so.*
%{_metainfodir}/*.appdata.xml
 
# opencv data
#{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/
 
%{_libdir}/libgstadaptivedemux-%{majorminor}.so.*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.*
%{_libdir}/libgstbadaudio-%{majorminor}.so.*
%{_libdir}/libgstcodecparsers-%{majorminor}.so.*
%{_libdir}/libgstcodecs-%{majorminor}.so.*
%{_libdir}/libgstinsertbin-%{majorminor}.so.*
%{_libdir}/libgstisoff-%{majorminor}.so.*
%{_libdir}/libgstmpegts-%{majorminor}.so.*
%{_libdir}/libgstplayer-%{majorminor}.so.*
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgstsctp-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%{_libdir}/libgstvulkan-%{majorminor}.so.*
%{_libdir}/libgstwebrtc-%{majorminor}.so.*
%if 0%{?fedora} || 0%{?rhel} > 7
%{_libdir}/libgstwayland-%{majorminor}.so.*
%endif
%{_libdir}/libgstopencv-%{majorminor}.so.*

	
%{_libdir}/girepository-1.0/GstBadAudio-1.0.typelib
%{_libdir}/girepository-1.0/GstCodecs-1.0.typelib
%{_libdir}/girepository-1.0/GstInsertBin-1.0.typelib
%{_libdir}/girepository-1.0/GstMpegts-1.0.typelib
%{_libdir}/girepository-1.0/GstPlayer-1.0.typelib
%{_libdir}/girepository-1.0/GstVulkan-1.0.typelib
%{_libdir}/girepository-1.0/GstWebRTC-1.0.typelib
%{_libdir}/girepository-1.0/GstVulkanWayland-1.0.typelib

# Plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstaccurip.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiobuffersplit.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiolatency.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixmatrix.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstdash.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvbsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaceoverlay.so
%if %{with extras}
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so
%endif
 
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 9
%{_libdir}/gstreamer-%{majorminor}/libgstfdkaac.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeverb.so
%{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
%{_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
%{_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{majorminor}/libgstlegacyrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
%{_libdir}/gstreamer-%{majorminor}/libgstipcpipeline.so
%{_libdir}/gstreamer-%{majorminor}/libgstinter.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstivfparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstivtc.so
%{_libdir}/gstreamer-%{majorminor}/libgstjp2kdecimator.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%{_libdir}/gstreamer-%{majorminor}/libgstmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%{_libdir}/gstreamer-%{majorminor}/libgstnetsim.so
%{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
%{_libdir}/gstreamer-%{majorminor}/libgstproxy.so
%{_libdir}/gstreamer-%{majorminor}/libgstremovesilence.so
%{_libdir}/gstreamer-%{majorminor}/libgstresindvd.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmanagerbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtponvif.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmooth.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstswitchbin.so
%{_libdir}/gstreamer-%{majorminor}/libgsttimecode.so
%{_libdir}/gstreamer-%{majorminor}/libgstuvch264.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoframe_audiolevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4mdec.so
 
# System (Linux) specific plugins
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%{_libdir}/gstreamer-%{majorminor}/libgstv4l2codecs.so
 
# Plugins with external dependencies
 
%{_libdir}/gstreamer-%{majorminor}/libgstaom.so
%{_libdir}/gstreamer-%{majorminor}/libgstbluez.so
%{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%{_libdir}/gstreamer-%{majorminor}/libgstclosedcaption.so
%{_libdir}/gstreamer-%{majorminor}/libgstcolormanagement.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtls.so
%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstkms.so
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%{_libdir}/gstreamer-%{majorminor}/libgstmicrodns.so
%{_libdir}/gstreamer-%{majorminor}/libgstnvcodec.so

%{_libdir}/gstreamer-%{majorminor}/libgstopusparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstrist.so
%{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%{_libdir}/gstreamer-%{majorminor}/libgstsoundtouch.so
%{_libdir}/gstreamer-%{majorminor}/libgstsrt.so
%{_libdir}/gstreamer-%{majorminor}/libgstsrtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstvulkan.so
%if 0%{?fedora} || 0%{?rhel} > 7
%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstwebp.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebrtc.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebrtcdsp.so
%if 0
%{_libdir}/gstreamer-%{majorminor}/libgstwpe.so
%endif
%if %{with extras}
%{_libdir}/gstreamer-%{majorminor}/libgstlv2.so
%{_libdir}/gstreamer-%{majorminor}/libgstttmlsubs.so
%endif
%if !%{with extras}
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstteletext.so
%endif
 
#debugging plugin
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so

%files gtk
# Plugins with external dependencies
# GStreamer gtk plugin was renamed to 'gtk'
# https://bugzilla.gnome.org/show_bug.cgi?id=779344
# https://github.com/GStreamer/gst-plugins-bad/commit/eb2dae8fd6aea04673fdd5b0fdf05e4e2ce1c2ee

# Now gstreamer1-plugins-good has libgstgtk.so
%{_libdir}/gstreamer-%{majorminor}/libgstgtksink.so 
 
%files extras
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstassrender.so
%{_libdir}/gstreamer-%{majorminor}/libgstbs2b.so
%{_libdir}/gstreamer-%{majorminor}/libgstchromaprint.so
%{_libdir}/gstreamer-%{majorminor}/libgstcurl.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
%{_libdir}/gstreamer-%{majorminor}/libgstgme.so
%{_libdir}/gstreamer-%{majorminor}/libgstkate.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstofa.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenal.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenexr.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstspandsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstteletext.so
%if 0%{?fedora} >= 31
%{_libdir}/gstreamer-%{majorminor}/libgstva.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenmpt.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstopencv.so

 
%files zbar
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstzbar.so
 
%files fluidsynth
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstfluidsynthmidi.so
 
%files wildmidi
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstwildmidi.so


 
%files devel
 
%{_datadir}/gir-1.0/GstBadAudio-%{majorminor}.gir
%{_datadir}/gir-1.0/GstCodecs-%{majorminor}.gir
%{_datadir}/gir-1.0/GstInsertBin-%{majorminor}.gir
%{_datadir}/gir-1.0/GstMpegts-%{majorminor}.gir
%{_datadir}/gir-1.0/GstPlayer-%{majorminor}.gir
%{_datadir}/gir-1.0/GstVulkan-%{majorminor}.gir
%{_datadir}/gir-1.0/GstWebRTC-%{majorminor}.gir
%{_datadir}/gir-1.0/GstVulkanWayland-1.0.gir

%{_libdir}/libgsttranscoder-%{majorminor}.so 
%{_libdir}/libgstadaptivedemux-%{majorminor}.so
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so
%{_libdir}/libgstbadaudio-%{majorminor}.so
%{_libdir}/libgstcodecparsers-%{majorminor}.so
%{_libdir}/libgstcodecs-%{majorminor}.so
%{_libdir}/libgstinsertbin-%{majorminor}.so
%{_libdir}/libgstisoff-%{majorminor}.so
%{_libdir}/libgstmpegts-%{majorminor}.so
%{_libdir}/libgstplayer-%{majorminor}.so
%{_libdir}/libgstphotography-%{majorminor}.so
%{_libdir}/libgstsctp-%{majorminor}.so
%{_libdir}/libgsturidownloader-%{majorminor}.so
%{_libdir}/libgstvulkan-%{majorminor}.so
%{_libdir}/libgstwebrtc-%{majorminor}.so
%if 0%{?fedora} || 0%{?rhel} > 7
%{_libdir}/libgstwayland-%{majorminor}.so
%endif
%{_libdir}/libgstopencv-%{majorminor}.so
 
%{_includedir}/gstreamer-%{majorminor}/gst/audio
%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc
%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers
%{_includedir}/gstreamer-%{majorminor}/gst/insertbin
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{majorminor}/gst/isoff/
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts
%{_includedir}/gstreamer-%{majorminor}/gst/player
%{_includedir}/gstreamer-%{majorminor}/gst/sctp
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader
%{_includedir}/gstreamer-%{majorminor}/gst/vulkan/
%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/
%{_includedir}/gstreamer-%{majorminor}/gst/opencv/gstopencvutils.h
%{_includedir}/gstreamer-%{majorminor}/gst/opencv/gstopencvvideofilter.h
%{_includedir}/gstreamer-%{majorminor}/gst/opencv/opencv-prelude.h
# Wtf?
#{_includedir}/include/gstreamer-1.0/gst/vulkan/vulkan-enumtypes.h 
 
# pkg-config files
%{_libdir}/pkgconfig/gstreamer-bad-audio-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-photography-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-player-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-sctp-%{majorminor}.pc
#%{_libdir}/pkgconfig/gstreamer-bad-transcoder-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-webrtc-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-wayland-1.0.pc


%changelog

* Thu Nov 05 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.1-9
- Rebuilt for opencv

* Thu Oct 29 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.1-7
- Updated to 1.18.1

* Wed Oct 07 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.0-9
- Restore libgsttranscoder libs

* Mon Oct 05 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.0-8
- Obsolete/Provide gst-transcoder

* Mon Sep 28 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.0-7
- Updated to 1.18.0

* Tue Aug 25 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.17.90-7
- Updated to 1.17.90

* Fri Aug 14 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.17.2-10
- Rebuilt for opencv

* Sun Jul 26 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.17.2-9
- Deleted gst-transcoder

* Sun Jul 26 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.17.2-8
- Deleted gst-transcoder 

* Fri Jul 10 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.17.2-7
- Updated to 1.17.2

* Wed Jul 08 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.2-9
- Rebuilt for aom
- Changed to meson

* Fri Mar 20 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.2-8
- Rebuilt

* Wed Dec 04 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.2-7
- Updated to 1.16.2

* Mon Oct 21 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.1-8
- Enabled av1 

* Mon Sep 02 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.1-7
- Updated to 1.16.1

* Thu Jun 13 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.0-8
- Enabled fdk-aac-free

* Fri Apr 19 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.0-7
- Updated to 1.16.0

* Wed Feb 27 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.15.2-7
- Updated to 1.15.2-7

* Fri Jan 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.15.1-7 
- Updated to 1.15.1

* Wed Oct 03 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.4-7 
- Updated to 1.14.4-7

* Mon Sep 17 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.3-7 
- Updated to 1.14.3-7

* Fri Jul 20 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.2-7 
- Updated to 1.14.2-7

* Mon May 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.1-7 
- Updated to 1.14.1-7

* Wed Mar 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.0-7 
- Updated to 1.14.0-7

* Fri Mar 16 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.13.91-7 
- Updated to 1.13.91-7

* Sun Mar 04 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.13.90-7  
- Updated to 1.13.90-7

* Fri Dec 08 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.4-7
- Updated to 1.12.4-7

* Sun Oct 29 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.3-8
- Rebuilt with mesa-libEGL #issue:https://github.com/UnitedRPMs/issues/issues/13

* Mon Sep 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.3-7
- Updated to 1.12.3-7

* Sun Aug 13 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.2-3
- Fixed issue with libreoffice-gtk3

* Thu Jul 20 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.2-2
- Updated to 1.12.2-2

* Sat Jun 24 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.1-2
- Updated to 1.12.1-2

* Thu May 25 2017 David Vásquez <davidva AT tutanota DOT com> 1.12.0-2
- Updated to 1.12.0-2

* Thu May 25 2017 David Vásquez <davidva AT tutanota DOT com> 1.11.91-3
- Rebuilt for libgstrawparse.so issue

* Sat Apr 29 2017 David Vásquez <davidva AT tutanota DOT com> 1.11.91-2
- Updated to 1.11.91-2

* Thu Apr 20 2017 David Vásquez <davidva AT tutanota DOT com> 1.11.90-2
- Updated to 1.11.90-2

* Thu Mar 30 2017 - David Vasquez <davidva AT tutanota DOT com>  1.11.2-3
- Rebuilt

* Wed Mar 22 2017 - David Vasquez <davidva AT tutanota DOT com>  1.11.2-2
- Upstream

* Fri Feb 24 2017 Wim Taymans <wtaymans@redhat.com> - 1.11.2-1
- Update to 1.11.2
- add audiomixmatrix

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 1.11.1-2
- Rebuild (libwebp)

* Fri Jan 13 2017 Wim Taymans <wtaymans@redhat.com> - 1.11.1-1
- Update to 1.11.1
- Add audiobuffersplit
- Dataurisrc was moved to core
- Add ttmlsubs plugin

* Mon Dec 05 2016 Wim Taymans <wtaymans@redhat.com> - 1.10.2-1
- Update to 1.10.2

* Mon Nov 28 2016 Wim Taymans <wtaymans@redhat.com> - 1.10.1-1
- Update to 1.10.1

* Thu Nov 03 2016 Wim Taymans <wtaymans@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Sat Oct 01 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.90-1
- Update to 1.9.90

* Fri Sep 02 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.2-2
- Rebuild

* Thu Sep 01 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.2-1
- Update to 1.9.2

* Fri Aug 26 2016 Hans de Goede <hdegoede@redhat.com> - 1.9.1-3
- Rebuild for new wildmidi

* Wed Aug 10 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.1-2
- Merge patches from Kevin Kofler (#1267665)
- Split gtksink into a -gtk subpackage (#1295444)
- Split wildmidi plugin into a -wildmidi subpackage (#1267665)
- BR mesa-libGLES-devel to enable OpenGL ES 2 support in GstGL (#1308290)

* Thu Jul 07 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.1-1
- Update to 1.9.1
- add musepack plugin
- add kmssink plugin

* Thu Jun 09 2016 Wim Taymans <wtaymans@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Sun May 08 2016 Wim Taymans <wtaymans@redhat.com> - 1.8.1-2
- Rebuild for opencv
- Disable opencv, the version is too new

* Thu Apr 21 2016 Wim Taymans <wtaymans@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Thu Mar 24 2016 Wim Taymans <wtaymans@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Wed Mar 16 2016 Wim Taymans <wtaymans@redhat.com> - 1.7.91-1
- Update to 1.7.91
- The opus parse was not moved so we still need opus-devel and we still
  ship a plugin.
- the plugin was renamed to opusparse

* Wed Mar 02 2016 Wim Taymans <wtaymans@redhat.com> - 1.7.90-1
- Update to 1.7.90
- the opus plugin was moved to -base.

* Thu Feb 25 2016 Wim Taymans <wtaymans@redhat.com> - 1.7.2-2
- Rebuild for soundtouch ABI break (#1311323)

* Fri Feb 19 2016 Wim Taymans <wtaymans@redhat.com> - 1.7.2-1
- Update to 1.7.2
- remove rtpbad plugin, it was moved
- add new libraries and netsim plugin

* Tue Feb 16 2016 Wim Taymans <wtaymans@redhat.com> - 1.7.1-5
- add chromaprint plugin

* Thu Feb 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.7.1-4
- Append -Dfatal-warnings to %%configure to prevent
  building from aborting for negligible warnings (Fix F24FTBFS)
- Append -Dsilent-rules to %%configure to make
  building verbose.
- Don't remove buildroot before installing.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 5 2016 Wim Taymans <wtaymans@redhat.com> - 1.7.1-2
- remove rpath from gtksink and mxf
- Fix description line too long

* Tue Jan 5 2016 Wim Taymans <wtaymans@redhat.com> - 1.7.1-1
- Update to 1.7.1
- rename fragmented -> hls
- remove liveadder
- add gstplayer
- add teletextdec and videoframe_audiolevel

* Mon Dec 28 2015 Rex Dieter <rdieter@fedoraproject.org> 1.6.2-2
- rebuild (libwebp)

* Tue Dec 15 2015 Wim Taymans <wtaymans@redhat.com> - 1.6.2-1
- Update to 1.6.2

* Mon Nov 9 2015 Wim Taymans <wtaymans@redhat.com> - 1.6.1-2
- Enable more plugins: gtksink, webp, bluez, bs2b, gme, ofa, openal,
  opencv, openjpeg

* Mon Nov 2 2015 Wim Taymans <wtaymans@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Remove lib64 rpaths from a few more libraries
- Use license macro for COPYING and COPYING.LIB

* Mon Sep 21 2015 Wim Taymans <wtaymans@redhat.com> - 1.5.91-1
- Update to 1.5.91

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 1.5.90-3
- Add optional data to AppStream metadata.

* Mon Aug 24 2015 Wim Taymans <wtaymans@redhat.com> - 1.5.90-2
- Enable uvch264

* Wed Aug 19 2015 Wim Taymans <wtaymans@redhat.com> - 1.5.90-1
- Update to 1.5.90

* Thu Jun 25 2015 Wim Taymans <wtaymans@redhat.com> - 1.5.2-1
- Update to 1.5.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Wim Taymans <wtaymans@redhat.com> - 1.5.1-1
- Update to 1.5.1
- Drop old patch

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.5-5
- Rebuilt for nettle soname bump

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.5-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 1.4.5-3
- Register as an AppStream component.

* Fri Mar 06 2015 David Woodhouse <dwmw2@infradead.org> - 1.4.5-2
- Fix RTP/RTCP muxing (#1199578)

* Tue Feb 03 2015 Wim Taymans <wtaymans@redhat.com> - 1.4.5-1
- Update to 1.4.5

* Tue Nov 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.4-2
- rebuild (openexr)

* Fri Nov 14 2014 Kalev Lember <kalevlember@gmail.com> - 1.4.4-1
- Update to 1.4.4

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 1.4.2-3
- Rebuild for new libsrtp

* Mon Sep 22 2014 Wim Taymans <wtaymans@redhat.com> - 1.4.2-2
- Remove celt buildreq, the plugin was removed and so is celt-devel

* Mon Sep 22 2014 Wim Taymans <wtaymans@redhat.com> - 1.4.2-1
- Update to 1.4.2.

* Fri Aug 29 2014 Wim Taymans <wtaymans@redhat.com> - 1.4.1-1
- Update to 1.4.1.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Wim Taymans <wtaymans@redhat.com> - 1.4.0-1
- Update to 1.4.0.

* Fri Jul 11 2014 Wim Taymans <wtaymans@redhat.com> - 1.3.91-1
- Update to 1.3.91.
- Remove old libraries

* Tue Jun 17 2014 Wim Taymans <wtaymans@redhat.com> - 1.2.4-1
- Update to 1.2.4.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Hans de Goede <hdegoede@}redhat.com> - 1.2.3-3
- Put the fluidsynth plugin in its own subpackage and make it require
  soundfont2-default (rhbz#1078925)

* Wed Mar 19 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.3-2
- Bump (libass)

* Mon Feb 10 2014 Brian Pepple <bpepple@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3.

* Thu Feb  6 2014 Brian Pepple <bpepple@fedoraproject.org> - 1.2.2-2
- Build the srtp plugin. (#1055669)

* Fri Dec 27 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2.

* Fri Nov 15 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-4
- Build fluidsynth plugin. (#1024906)

* Thu Nov 14 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-3
- Add BR on gnutls-devel for HLS support. (#1030491)

* Mon Nov 11 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-2
- Build ladspa, libkate, and wildmidi plugins.

* Mon Nov 11 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1.

* Fri Nov  8 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.0-3
- Build gobject-introspection support. (#1028156)

* Fri Oct 04 2013 Bastien Nocera <bnocera@redhat.com> 1.2.0-2
- Build the wayland video output plugin

* Tue Sep 24 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0.

* Thu Sep 19 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.1.90-1
- Update to 1.1.90.

* Wed Aug 28 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4.

* Mon Jul 29 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3.

* Fri Jul 12 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2.

* Tue May 07 2013 Colin Walters <walters@verbum.org> - 1.0.7-2
- Move libgstdecklink to its correct place in extras; needed for RHEL

* Fri Apr 26 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7.

* Sun Mar 24 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6.
- Drop BR on PyXML.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Wed Dec 19 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Wed Nov 21 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Thu Oct 25 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Sun Oct  7 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1
- Add frei0r plugin to file list.

* Mon Oct  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-3
- Enable verbose build

* Wed Sep 26 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.0-2
- Build opus plugin.

* Mon Sep 24 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0.

* Thu Sep 20 2012 Bastien Nocera <bnocera@redhat.com> 0.11.99-2
- The soundtouch-devel BR should be on, even with extras disabled

* Wed Sep 19 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.99-1
- Update to 0.11.99

* Fri Sep 14 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.94-1
- Update to 0.11.94.

* Sat Aug 18 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.93-2
- Fix permission on tarball clean-up script.
- Re-enable soundtouch-devel.
- Add COPYING.LIB to package.
- Use %%global instead of %%define.

* Wed Aug 15 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.93-1
- Update to 0.11.93.

* Fri Jul 20 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.92-1
- Initial Fedora spec file.
