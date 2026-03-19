[app]
title = CENAD
package.name = cenad
package.domain = mg.cenad

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

version = 1.0.0

requirements = python3,kivy==2.3.0,pandas,numpy,matplotlib,scipy,pillow

orientation = portrait
fullscreen = 0

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = armeabi-v7a

android.allow_backup = True
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
