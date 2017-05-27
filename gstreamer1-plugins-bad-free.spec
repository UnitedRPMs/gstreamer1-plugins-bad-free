%global         majorminor 1.0
%global         _gobject_introspection  1.31.1

# Turn of extras package on RHEL.
%if ! 0%{?rhel}
%bcond_without extras
%else
%bcond_with extras
%endif

Name:           gstreamer1-plugins-bad-free
Version:        1.12.0
Release:        2%{?gitcommit:.git%{shortcommit}}%{?dist}
Summary:        GStreamer streaming media framework "bad" plugins

License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
Source1:        gst-p-bad-cleanup.sh

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel >= %{_gobject_introspection}

BuildRequires:  bzip2-devel
BuildRequires:  exempi-devel
BuildRequires:  gsm-devel
BuildRequires:  jasper-devel
BuildRequires:  ladspa-devel
BuildRequires:  libdvdnav-devel
BuildRequires:  libexif-devel
BuildRequires:  libiptcdata-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  liboil-devel
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
%if 0%{?fedora}
BuildRequires:  libwayland-client-devel
%endif
BuildRequires:  gnutls-devel
BuildRequires:  libsrtp-devel
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  gtk3-devel >= 3.4
BuildRequires:  bluez-libs-devel >= 5.0
BuildRequires:  libwebp-devel

BuildRequires:  chrpath

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
BuildRequires:  game-music-emu-devel
BuildRequires:  libkate-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libofa-devel
## Plugins not ported
#BuildRequires:  libmusicbrainz-devel
#BuildRequires:  libtimidity-devel
BuildRequires:  libvdpau-devel
BuildRequires:  openal-soft-devel
#BuildRequires:  opencv-devel
BuildRequires:  openjpeg-devel
BuildRequires:  schroedinger-devel
## Plugins not ported
#BuildRequires:  SDL-devel
#BuildRequires:  slv2-devel
BuildRequires:  wildmidi-devel
BuildRequires:  zbar-devel
BuildRequires:  zvbi-devel
BuildRequires:  OpenEXR-devel
%endif


%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested well enough, or the code
is not of good enough quality.

%package gtk
Summary:         GStreamer "bad" plugins gtk plugin
Requires:        %{name} = %{version}-%{release}

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

%build
%configure --disable-fatal-warnings \
    --with-package-name="Fedora GStreamer-plugins-bad package" \
    --with-package-origin="http://download.fedoraproject.org" \
    %{!?with_extras:--disable-fbdev --disable-decklink --disable-linsys} \
    --enable-debug --disable-static --enable-gtk-doc --enable-experimental \
    --disable-dts --disable-faac --disable-faad --disable-nas \
    --disable-mimic --disable-libmms --disable-mpeg2enc --disable-mplex \
    --disable-neon --disable-rtmp --disable-xvid \
    --disable-flite --disable-mpg123 --disable-sbc --disable-opencv --enable-silent-rules \
    --disable-spandsp --disable-voamrwbenc --disable-x265  

# https://bugzilla.gnome.org/show_bug.cgi?id=655517
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
 
make %{?_smp_mflags} V=0


%install
make install DESTDIR=%{buildroot}/

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}/%{_datadir}/appdata
cat > %{buildroot}/%{_datadir}/appdata/gstreamer-bad-free.appdata.xml <<EOF
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
find %{buildroot}/ -name '*.la' -exec rm -f {} ';'
# Kill rpath
# chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
# chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstcompositor.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdashdemux.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
# chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstgtksink.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstopengl.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstuvch264.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstvdpau.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
chrpath --delete %{buildroot}/%{_libdir}/libgstadaptivedemux-%{majorminor}.so
chrpath --delete %{buildroot}/%{_libdir}/libgstbadvideo-%{majorminor}.so

# chrpath --delete %{buildroot}/%{_libdir}/libgstbadaudio-1.0.so.0.1190.0
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstgtk.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
# chrpath --delete %{buildroot}/%{_libdir}/libgstgl-1.0.so.0.1190.0
# chrpath --delete %{buildroot}/%{_libdir}/libgstbadallocators-1.0.so.0.1190.0
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
chrpath --delete %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstopenjpeg.so

#chrpath --delete %{buildroot}/%{_libdir}/libgstbadaudio-1.0.so.0.1191.0
# chrpath --delete %{buildroot}/%{_libdir}/libgstgl-1.0.so.0.1191.0
chrpath --delete %{buildroot}/%{_libdir}/libgstgl-1.0.so.0.1200.0

# It is provided by freeworld, we don't need it here
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdvbsuboverlay.so 
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so 
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstfdkaac.so 
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstopenh264.so
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstqmlgl.so 
rm -f %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstsiren.so 
#


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files -f gst-plugins-bad-%{majorminor}.lang
%license COPYING COPYING.LIB
%doc AUTHORS README REQUIREMENTS

%{_datadir}/appdata/*.appdata.xml

# presets
%dir %{_datadir}/gstreamer-%{majorminor}/presets/
%{_datadir}/gstreamer-%{majorminor}/presets/GstFreeverb.prs

# opencv data
#%dir %{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/
#%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/fist.xml
#%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/palm.xml

%{_libdir}/libgstadaptivedemux-%{majorminor}.so.*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.*
%{_libdir}/libgstbadallocators-%{majorminor}.so.*
%{_libdir}/libgstbadaudio-%{majorminor}.so.*
%{_libdir}/libgstbadbase-%{majorminor}.so.*
%{_libdir}/libgstbadvideo-%{majorminor}.so.*
%{_libdir}/libgstcodecparsers-%{majorminor}.so.*
%{_libdir}/libgstgl-%{majorminor}.so.*
%{_libdir}/libgstinsertbin-%{majorminor}.so.*
%{_libdir}/libgstmpegts-%{majorminor}.so.*
%{_libdir}/libgstplayer-%{majorminor}.so.*
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%if 0%{?fedora}
%{_libdir}/libgstwayland-%{majorminor}.so.*
%endif
%{_libdir}/girepository-1.0/GstGL-1.0.typelib
%{_libdir}/girepository-1.0/GstInsertBin-1.0.typelib
%{_libdir}/girepository-1.0/GstMpegts-1.0.typelib
%{_libdir}/girepository-1.0/GstPlayer-1.0.typelib
%{_libdir}/girepository-1.0/GstBadAllocators-1.0.typelib

# Plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstaccurip.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiobuffersplit.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixmatrix.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstcompositor.so
%{_libdir}/gstreamer-%{majorminor}/libgstdashdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaceoverlay.so
%if %{with extras}
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeverb.so
%{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
%{_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
%{_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
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
# libgstrawparse.so is provided by gstreamer1-plugins-base
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstlegacyrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstremovesilence.so
%{_libdir}/gstreamer-%{majorminor}/libgstresindvd.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtponvif.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmooth.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgststereo.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgsttimecode.so
%{_libdir}/gstreamer-%{majorminor}/libgstuvch264.so
%if %{with extras}
%{_libdir}/gstreamer-%{majorminor}/libgstvdpau.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoframe_audiolevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so
%{_libdir}/gstreamer-%{majorminor}/libgstyadif.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4mdec.so

# System (Linux) specific plugins
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%{_libdir}/gstreamer-%{majorminor}/libgstvcdsrc.so

# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtls.so
%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so
%{_libdir}/gstreamer-%{majorminor}/libgstkms.so
%{_libdir}/gstreamer-%{majorminor}/libgstopengl.so
%{_libdir}/gstreamer-%{majorminor}/libgstopusparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%{_libdir}/gstreamer-%{majorminor}/libgstsoundtouch.so
%{_libdir}/gstreamer-%{majorminor}/libgstsrtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstttmlsubs.so
%if 0%{?fedora}
%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstwebp.so

#debugging plugin
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so


%files gtk
# Plugins with external dependencies
# GStreamer gtk plugin was renamed to 'gtk'
# https://bugzilla.gnome.org/show_bug.cgi?id=779344
# https://github.com/GStreamer/gst-plugins-bad/commit/eb2dae8fd6aea04673fdd5b0fdf05e4e2ce1c2ee
%{_libdir}/gstreamer-%{majorminor}/libgstgtk.so
%{_libdir}/gstreamer-%{majorminor}/libgstgtksink.so


%if %{with extras}
%files extras
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstassrender.so
%{_libdir}/gstreamer-%{majorminor}/libgstbluez.so
%{_libdir}/gstreamer-%{majorminor}/libgstbs2b.so
%{_libdir}/gstreamer-%{majorminor}/libgstchromaprint.so
%{_libdir}/gstreamer-%{majorminor}/libgstcurl.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
%{_libdir}/gstreamer-%{majorminor}/libgstgme.so
%{_libdir}/gstreamer-%{majorminor}/libgstkate.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstofa.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenal.so
#%{_libdir}/gstreamer-%{majorminor}/libgstopencv.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenexr.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstschro.so
#%{_libdir}/gstreamer-%{majorminor}/libgstteletextdec.so
#%{_libdir}/gstreamer-%{majorminor}/libgstteletex.so
%{_libdir}/gstreamer-%{majorminor}/libgstzbar.so
%{_libdir}/gstreamer-1.0/libgstteletext.so


%files fluidsynth
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstfluidsynthmidi.so

%files wildmidi
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstwildmidi.so
%endif


%files devel
%doc %{_datadir}/gtk-doc/html/gst-plugins-bad-plugins-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gst-plugins-bad-libs-%{majorminor}

%{_datadir}/gir-1.0/GstGL-1.0.gir
%{_datadir}/gir-1.0/GstInsertBin-%{majorminor}.gir
%{_datadir}/gir-1.0/GstMpegts-%{majorminor}.gir
%{_datadir}/gir-1.0/GstPlayer-%{majorminor}.gir
%{_datadir}/gir-1.0/GstBadAllocators-1.0.gir

%{_libdir}/libgstadaptivedemux-%{majorminor}.so
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so
%{_libdir}/libgstbadaudio-%{majorminor}.so
%{_libdir}/libgstbadbase-%{majorminor}.so
%{_libdir}/libgstbadvideo-%{majorminor}.so
%{_libdir}/libgstcodecparsers-%{majorminor}.so
%{_libdir}/libgstgl-%{majorminor}.so
%{_libdir}/libgstinsertbin-%{majorminor}.so
%{_libdir}/libgstmpegts-%{majorminor}.so
%{_libdir}/libgstplayer-%{majorminor}.so
%{_libdir}/libgstphotography-%{majorminor}.so
%{_libdir}/libgsturidownloader-%{majorminor}.so
%if 0%{?fedora}
%{_libdir}/libgstwayland-%{majorminor}.so
%endif
%{_libdir}/libgstbadallocators-%{majorminor}.so
%{_libdir}/gstreamer-%{majorminor}/include/gst/gl/gstglconfig.h

%{_includedir}/gstreamer-%{majorminor}/gst/audio
%{_includedir}/gstreamer-%{majorminor}/gst/base
%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc
%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers
%{_includedir}/gstreamer-%{majorminor}/gst/insertbin
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts
%{_includedir}/gstreamer-%{majorminor}/gst/player
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader
%{_includedir}/gstreamer-%{majorminor}/gst/gl
%{_includedir}/gstreamer-%{majorminor}/gst/video
%{_includedir}/gstreamer-1.0/gst/allocators/badallocators.h
%{_includedir}/gstreamer-1.0/gst/allocators/gstphysmemory.h

# pkg-config files
%{_libdir}/pkgconfig/gstreamer-bad-audio-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-bad-base-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-bad-video-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-gl-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-player-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-bad-allocators-1.0.pc

%changelog

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
- Append --disable-fatal-warnings to %%configure to prevent
  building from aborting for negligible warnings (Fix F24FTBFS)
- Append --disable-silent-rules to %%configure to make
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
