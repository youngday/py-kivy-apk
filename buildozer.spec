[app]

# (str) Title of your application
title = Calculator

# (str) Package name
package.name = calculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using glob patterns
source.include_globs = *.py

# (list) List of exclusions using glob patterns
source.exclude_globs = *.pyc

# (str) Application version (from main.py __version__)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = python3,kivy==2.3.1

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
android.api = 34

# (str) Android build tools version
android.build_tools = 34.0.0

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use (use system pre-installed NDK)
android.ndk = 27.3.13750724

# (str) Path to Android SDK (system pre-installed)
android.sdk_path = /usr/local/lib/android/sdk

# (str) Path to Android NDK
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

# (str) Python-for-android (p4a) branch to use
p4a.branch = develop

# (str) Android package name (must be unique)
android.package_name = org.example.calculator

# (str) Android activity name (must be unique)
android.activity_name = CalculatorActivity

# (list) Supported orientations
android.orientations = portrait

# (str) The Android arch to build for: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (str) JDK version to use
android.jdk = 17

# (bool) Enable AndroidX (Android only)
android.use_androidx = True

# (bool) Use Gradle instead of ant
android.gradle = True

# (bool) Enable multidex?
android.multidex = True

# (str) Android app theme
android.app_theme = @android:style/Theme.Material.Light.NoActionBar

# (bool) Build the APK in debug mode
android.debug = True

# (str) Log level for buildozer (default: info)
#buildozer.log_level = 2

# (int) Number of parallel build jobs (default: number of CPU cores - 1)
#buildozer.parallel_jobs = 2