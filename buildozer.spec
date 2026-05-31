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

# (list) List of additional assets to include
source.extra_globs =

# (str) Application version
version = 0.1.0

# (str) Application versioning method
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1

# (str) Custom source folders for requirements
#requirements.source.kivy = /path/to/kivy

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
android.api = 34

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use Android's default Java 8? (requires Android 8+)
android.use_default_java8 = True

# (str) Python-for-android (p4a) branch to use (default: master)
p4a.branch = develop

# (str) Android package name (must be unique)
android.package_name = org.example.calculator

# (str) Android activity name (must be unique)
android.activity_name = CalculatorActivity

# (str) Presplash background color (Android only)
#android.presplash_color = #FFFFFF

# (str) Presplash image
#android.presplash_image = path/to/presplash.png

# (str) Icon
#android.icon = path/to/icon.png

# (list) Supported orientations
android.orientations = portrait

# (list) Metadata
#android.meta_data = key=value,other=value

# (list) Java libraries to add
#android.add_jars = foo.jar,bar.jar

# (bool) Enable Google Play Services
#android.google_play_services = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) Override the default version of CMake
#android.cmake_version = 3.10.2

# (str) JDK version to use
android.jdk = 17

# (str) Path to the Android SDK
#android.sdk_path = /home/user/android-sdk

# (str) Path to the Android NDK
#android.ndk_path = /home/user/android-ndk

# (str) Path to the Android Ant
#android.ant_path = /usr/share/ant

# (str) Android Gradle plugin version (Android only)
#android.gradle_plugin_version = 4.1.0

# (bool) Enable AndroidX (Android only)
#android.use_androidx = True

# (str) Extra command line arguments for buildozer
#buildozer.extra_args = --enable-crypt

# (bool) Enable the use of TMPDIR for temporary files
#buildozer.tmpdir =

# (str) Log level for buildozer (default: info)
#buildozer.log_level = 2

# (int) Number of parallel build jobs (default: number of CPU cores - 1)
#buildozer.parallel_jobs = 2

# (bool) Use Gradle instead of ant (recommended)
#android.gradle = True

# (str) Path to the Gradle executable
#android.gradle_path = /usr/local/bin/gradle

# (bool) Sign APK? (default: False)
#android.sign_apk = False

# (str) Path to the keystore
#android.keystore = /path/to/keystore

# (str) Keystore password
#android.keyalias =

# (str) Key alias
#android.keystore_password =

# (str) Key password
#android.key_alias_password =

# (list) Additional source dirs (relative to source.dir)
#android.add_src =

# (str) Android app theme
android.app_theme = @android:style/Theme.Material.Light.NoActionBar

# (list) Support libraries to add
#android.support_libs =

# (list) Gradle dependencies
#android.gradle_dependencies =

# (bool) Enable Google Play Billing? (requires google-play-services)
#android.google_play_billing = False

# (bool) Enable Google Play Licensing? (requires google-play-services)
#android.google_play_licensing = False

# (bool) Enable AndroidX? (Android only)
#android.use_androidx = True

# (bool) Enable multidex?
#android.multidex = True

# (int) Minimum SDK version for AndroidX
#android.minimum_sdk_version = 21

# (bool) Enable the use of a Python virtual environment on target device?
#android.use_virtualenv = False

# (str) Path to the virtual environment on target device
#android.virtualenv_path = /data/data/org.example.calculator/files/venv

# (str) The path to the virtual environment on the host
#android.virtualenv_host_path = /path/to/venv

# (str) The path to the Python executable on the host
#android.python_host_path = /usr/bin/python3

# (bool) Enable the use of a compiled Python on target device
#android.compiled_python = True

# (bool) Build the APK in debug mode
#android.debug = True

# (list) Android extra libraries to include (e.g., libcrypto.so)
#android.extra_libs =

# (list) Android extra Java files
#android.extra_java_files =

# (str) Android app theme (for gradle)
#android.app_theme_gradle = @style/AppTheme

# (bool) Enable the use of a custom AndroidManifest.xml
#android.use_custom_manifest = False

# (bool) Enable the use of a custom build.gradle
#android.use_custom_gradle = False

# (bool) Enable the use of a custom build.gradle.kts
#android.use_custom_gradle_kts = False

# (bool) Enable the use of a custom Android.mk
#android.use_custom_mk = False

# (str) Path to the custom AndroidManifest.xml
#android.custom_manifest_path = /path/to/AndroidManifest.xml

# (str) Path to the custom build.gradle
#android.custom_gradle_path = /path/to/build.gradle

# (str) Path to the custom build.gradle.kts
#android.custom_gradle_kts_path = /path/to/build.gradle.kts

# (str) Path to the custom Android.mk
#android.custom_mk_path = /path/to/Android.mk

# (str) The architecture to build for on Android
#android.arch = arm64-v8a

# (bool) Use the latest changes of kivy/python-for-android?
#android.use_latest_p4a = False

# (bool) Enable the use of a custom Android SDK platform (default: False)
#android.use_custom_sdk = False

# (str) Path to the custom Android SDK platform
#android.custom_sdk_path = /path/to/sdk

# (str) Path to the custom Android NDK
#android.custom_ndk_path = /path/to/ndk

# (str) Path to the custom Apache Ant
#android.custom_ant_path = /path/to/ant

# (str) Path to the custom Gradle
#android.custom_gradle_path = /path/to/gradle

# (str) Path to the custom Maven
#android.custom_maven_path = /path/to/maven

# (bool) Enable the use of a custom Maven repository
#android.use_custom_maven_repo = False

# (str) Path to the custom Maven repository
#android.custom_maven_repo_path = /path/to/maven-repo

# (bool) Enable the use of a custom Python-for-android recipe repo
#android.use_custom_p4a_repo = False

# (str) Path to the custom Python-for-android recipe repo
#android.custom_p4a_repo_path = /path/to/p4a-repo

# (list) Additional Python-for-android recipes to include
#android.p4a_recipes =

# (list) Additional Python-for-android patches
#android.p4a_patches =

# (str) The name of the Python-for-android branch to use
#android.p4a_branch = develop

# (str) The Python-for-android commit hash to use
#android.p4a_commit =

# (bool) Enable the use of a custom Python-for-android egg
#android.use_custom_p4a_egg = False

# (str) Path to the custom Python-for-android egg
#android.custom_p4a_egg_path = /path/to/p4a-egg

# (bool) Enable the use of a custom Android virtual device
#android.use_custom_avd = False

# (str) Path to the custom Android virtual device
#android.custom_avd_path = /path/to/avd

# (bool) Enable the use of a custom Android emulator
#android.use_custom_emulator = False

# (str) Path to the custom Android emulator
#android.custom_emulator_path = /path/to/emulator

# (bool) Enable the use of a custom Android device
#android.use_custom_device = False

# (str) Path to the custom Android device
#android.custom_device_path = /path/to/device

# (list) Android extra libraries to include
#android.extra_libs =

# (bool) Enable the use of a custom Android library
#android.use_custom_library = False

# (str) Path to the custom Android library
#android.custom_library_path = /path/to/library

# (list) Android extra Java files
#android.extra_java_files =

# (bool) Enable the use of a custom Java file
#android.use_custom_java = False

# (str) Path to the custom Java file
#android.custom_java_path = /path/to/Java

# (bool) Enable the use of a custom Android resource
#android.use_custom_resource = False

# (str) Path to the custom Android resource
#android.custom_resource_path = /path/to/resource

# (bool) Enable the use of a custom Android asset
#android.use_custom_asset = False

# (str) Path to the custom Android asset
#android.custom_asset_path = /path/to/asset

# (bool) Enable the use of a custom Android library
#android.use_custom_library = False

# (str) Path to the custom Android library
#android.custom_library_path = /path/to/library

# (list) Android extra jars
#android.extra_jars =

# (list) Android extra aars
#android.extra_aars =

# (bool) Enable the use of a custom Android native library
#android.use_custom_native_library = False

# (str) Path to the custom Android native library
#android.custom_native_library_path = /path/to/native

# (bool) Enable the use of a custom Python-for-android recipe
#android.use_custom_p4a_recipe = False

# (str) Path to the custom Python-for-android recipe
#android.custom_p4a_recipe_path = /path/to/p4a-recipe

# (bool) Enable the use of a custom Python-for-android patch
#android.use_custom_p4a_patch = False

# (str) Path to the custom Python-for-android patch
#android.custom_p4a_patch_path = /path/to/p4a-patch

# (bool) Enable the use of a custom Android virtual device
#android.use_custom_avd = False

# (str) Path to the custom Android virtual device
#android.custom_avd_path = /path/to/avd

# (bool) Enable the use of a custom Android emulator
#android.use_custom_emulator = False

# (str) Path to the custom Android emulator
#android.custom_emulator_path = /path/to/emulator

# (bool) Enable the use of a custom Android device
#android.use_custom_device = False

# (str) Path to the custom Android device
#android.custom_device_path = /path/to/device

# (str) Android NDK version (for p4a)
#android.ndk_version = 23b

# (list) Android SDK platforms to download
#android.sdk_platforms = 34

# (list) Android build tools version
#android.build_tools = 34.0.0

# (list) Android cmake version
#android.cmake_version = 3.22.1

# (bool) Use the default Android SDK manager
#android.use_sdk_manager = True

# (str) Path to the Android SDK manager
#android.sdk_manager_path = /usr/local/bin/sdkmanager

# (bool) Enable the use of a custom Android SDK manager
#android.use_custom_sdk_manager = False

# (str) Path to the custom Android SDK manager
#android.custom_sdk_manager_path = /path/to/sdkmanager

# (str) Android NDK version (for p4a)
#android.ndk_version = 23b

# (list) Android SDK platforms to download
#android.sdk_platforms = 34

# (list) Android build tools version
#android.build_tools = 34.0.0

# (list) Android cmake version
#android.cmake_version = 3.22.1

# (bool) Use the default Android SDK manager
#android.use_sdk_manager = True

# (str) Path to the Android SDK manager
#android.sdk_manager_path = /usr/local/bin/sdkmanager

# (bool) Enable the use of a custom Android SDK manager
#android.use_custom_sdk_manager = False

# (str) Path to the custom Android SDK manager
#android.custom_sdk_manager_path = /path/to/sdkmanager

# (int) Android API level to target
android.api = 34

# (int) Minimum API level required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use Android's default Java 8? (requires Android 8+)
android.use_default_java8 = True

# (str) Python-for-android (p4a) branch to use (default: master)
p4a.branch = develop

# (str) Android package name (must be unique)
android.package_name = org.example.calculator

# (str) Android activity name (must be unique)
android.activity_name = CalculatorActivity

# (str) Presplash background color (Android only)
#android.presplash_color = #FFFFFF

# (str) Presplash image
#android.presplash_image = path/to/presplash.png

# (str) Icon
#android.icon = path/to/icon.png

# (list) Supported orientations
android.orientations = portrait

# (list) Metadata
#android.meta_data = key=value,other=value

# (list) Java libraries to add
#android.add_jars = foo.jar,bar.jar

# (bool) Enable Google Play Services
#android.google_play_services = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) Override the default version of CMake
#android.cmake_version = 3.10.2

# (str) JDK version to use
android.jdk = 17

# (str) Path to the Android SDK
#android.sdk_path = /home/user/android-sdk

# (str) Path to the Android NDK
#android.ndk_path = /home/user/android-ndk

# (str) Path to the Android Ant
#android.ant_path = /usr/share/ant

# (str) Android Gradle plugin version (Android only)
#android.gradle_plugin_version = 4.1.0

# (bool) Enable AndroidX (Android only)
#android.use_androidx = True

# (str) Extra command line arguments for buildozer
#buildozer.extra_args = --enable-crypt

# (bool) Enable the use of TMPDIR for temporary files
#buildozer.tmpdir =

# (str) Log level for buildozer (default: info)
#buildozer.log_level = 2

# (int) Number of parallel build jobs (default: number of CPU cores - 1)
#buildozer.parallel_jobs = 2

# (bool) Use Gradle instead of ant (recommended)
#android.gradle = True

# (str) Path to the Gradle executable
#android.gradle_path = /usr/local/bin/gradle

# (bool) Sign APK? (default: False)
#android.sign_apk = False

# (str) Path to the keystore
#android.keystore = /path/to/keystore

# (str) Keystore password
#android.keyalias =

# (str) Key alias
#android.keystore_password =

# (str) Key password
#android.key_alias_password =

# (list) Additional source dirs (relative to source.dir)
#android.add_src =

# (str) Android app theme
android.app_theme = @android:style/Theme.Material.Light.NoActionBar

# (list) Support libraries to add
#android.support_libs =

# (list) Gradle dependencies
#android.gradle_dependencies =

# (bool) Enable Google Play Billing? (requires google-play-services)
#android.google_play_billing = False

# (bool) Enable Google Play Licensing? (requires google-play-services)
#android.google_play_licensing = False

# (bool) Enable AndroidX? (Android only)
#android.use_androidx = True

# (bool) Enable multidex?
#android.multidex = True

# (int) Minimum SDK version for AndroidX
#android.minimum_sdk_version = 21

# (bool) Enable the use of a Python virtual environment on target device?
#android.use_virtualenv = False

# (str) Path to the virtual environment on target device
#android.virtualenv_path = /data/data/org.example.calculator/files/venv

# (str) The path to the virtual environment on the host
#android.virtualenv_host_path = /path/to/venv

# (str) The path to the Python executable on the host
#android.python_host_path = /usr/bin/python3

# (bool) Enable the use of a compiled Python on target device
#android.compiled_python = True

# (bool) Build the APK in debug mode
#android.debug = True

# (list) Android extra libraries to include (e.g., libcrypto.so)
#android.extra_libs =

# (list) Android extra Java files
#android.extra_java_files =

# (str) Android app theme (for gradle)
#android.app_theme_gradle = @style/AppTheme

# (bool) Enable the use of a custom AndroidManifest.xml
#android.use_custom_manifest = False

# (bool) Enable the use of a custom build.gradle
#android.use_custom_gradle = False

# (bool) Enable the use of a custom build.gradle.kts
#android.use_custom_gradle_kts = False

# (bool) Enable the use of a custom Android.mk
#android.use_custom_mk = False

# (str) Path to the custom AndroidManifest.xml
#android.custom_manifest_path = /path/to/AndroidManifest.xml

# (str) Path to the custom build.gradle
#android.custom_gradle_path = /path/to/build.gradle

# (str) Path to the custom build.gradle.kts
#android.custom_gradle_kts_path = /path/to/build.gradle.kts

# (str) Path to the custom Android.mk
#android.custom_mk_path = /path/to/Android.mk

# (str) The architecture to build for on Android
#android.arch = arm64-v8a

# (bool) Use the latest changes of kivy/python-for-android?
#android.use_latest_p4a = False

# (bool) Enable the use of a custom Android SDK platform (default: False)
#android.use_custom_sdk = False

# (str) Path to the custom Android SDK platform
#android.custom_sdk_path = /path/to/sdk

# (str) Path to the custom Android NDK
#android.custom_ndk_path = /path/to/ndk

# (str) Path to the custom Apache Ant
#android.custom_ant_path = /path/to/ant

# (str) Path to the custom Gradle
#android.custom_gradle_path = /path/to/gradle

# (str) Path to the custom Maven
#android.custom_maven_path = /path/to/maven

# (bool) Enable the use of a custom Maven repository
#android.use_custom_maven_repo = False

# (str) Path to the custom Maven repository
#android.custom_maven_repo_path = /path/to/maven-repo

# (bool) Enable the use of a custom Python-for-android recipe repo
#android.use_custom_p4a_repo = False

# (str) Path to the custom Python-for-android recipe repo
#android.custom_p4a_repo_path = /path/to/p4a-repo

# (list) Additional Python-for-android recipes to include
#android.p4a_recipes =

# (list) Additional Python-for-android patches
#android.p4a_patches =

# (str) The name of the Python-for-android branch to use
#android.p4a_branch = develop

# (str) The Python-for-android commit hash to use
#android.p4a_commit =

# (bool) Enable the use of a custom Python-for-android egg
#android.use_custom_p4a_egg = False

# (str) Path to the custom Python-for-android egg
#android.custom_p4a_egg_path = /path/to/p4a-egg

# (bool) Enable the use of a custom Android virtual device
#android.use_custom_avd = False

# (str) Path to the custom Android virtual device
#android.custom_avd_path = /path/to/avd

# (bool) Enable the use of a custom Android emulator
#android.use_custom_emulator = False

# (str) Path to the custom Android emulator
#android.custom_emulator_path = /path/to/emulator

# (bool) Enable the use of a custom Android device
#android.use_custom_device = False

# (str) Path to the custom Android device
#android.custom_device_path = /path/to/device

# (list) Android extra libraries to include
#android.extra_libs =

# (bool) Enable the use of a custom Android library
#android.use_custom_library = False

# (str) Path to the custom Android library
#android.custom_library_path = /path/to/library

# (list) Android extra Java files
#android.extra_java_files =

# (bool) Enable the use of a custom Java file
#android.use_custom_java = False

# (str) Path to the custom Java file
#android.custom_java_path = /path/to/Java

# (bool) Enable the use of a custom Android resource
#android.use_custom_resource = False

# (str) Path to the custom Android resource
#android.custom_resource_path = /path/to/resource

# (bool) Enable the use of a custom Android asset
#android.use_custom_asset = False

# (str) Path to the custom Android asset
#android.custom_asset_path = /path/to/asset

# (bool) Enable the use of a custom Android library
#android.use_custom_library = False

# (str) Path to the custom Android library
#android.custom_library_path = /path/to/library

# (list) Android extra jars
#android.extra_jars =

# (list) Android extra aars
#android.extra_aars =

# (bool) Enable the use of a custom Android native library
#android.use_custom_native_library = False

# (str) Path to the custom Android native library
#android.custom_native_library_path = /path/to/native

# (bool) Enable the use of a custom Python-for-android recipe
#android.use_custom_p4a_recipe = False

# (str) Path to the custom Python-for-android recipe
#android.custom_p4a_recipe_path = /path/to/p4a-recipe

# (bool) Enable the use of a custom Python-for-android patch
#android.use_custom_p4a_patch = False

# (str) Path to the custom Python-for-android patch
#android.custom_p4a_patch_path = /path/to/p4a-patch

# (bool) Enable the use of a custom Android virtual device
#android.use_custom_avd = False

# (str) Path to the custom Android virtual device
#android.custom_avd_path = /path/to/avd

# (bool) Enable the use of a custom Android emulator
#android.use_custom_emulator = False

# (str) Path to the custom Android emulator
#android.custom_emulator_path = /path/to/emulator

# (bool) Enable the use of a custom Android device
#android.use_custom_device = False

# (str) Path to the custom Android device
#android.custom_device_path = /path/to/device

# (str) Android NDK version (for p4a)
#android.ndk_version = 23b

# (list) Android SDK platforms to download
#android.sdk_platforms = 34

# (list) Android build tools version
#android.build_tools = 34.0.0

# (list) Android cmake version
#android.cmake_version = 3.22.1

# (bool) Use the default Android SDK manager
#android.use_sdk_manager = True

# (str) Path to the Android SDK manager
#android.sdk_manager_path = /usr/local/bin/sdkmanager

# (bool) Enable the use of a custom Android SDK manager
#android.use_custom_sdk_manager = False

# (str) Path to the custom Android SDK manager
#android.custom_sdk_manager_path = /path/to/sdkmanager

# (str) Android NDK version (for p4a)
#android.ndk_version = 23b

# (list) Android SDK platforms to download
#android.sdk_platforms = 34

# (list) Android build tools version
#android.build_tools = 34.0.0

# (list) Android cmake version
#android.cmake_version = 3.22.1

# (bool) Use the default Android SDK manager
#android.use_sdk_manager = True

# (str) Path to the Android SDK manager
#android.sdk_manager_path = /usr/local/bin/sdkmanager

# (bool) Enable the use of a custom Android SDK manager
#android.use_custom_sdk_manager = False

# (str) Path to the custom Android SDK manager
#android.custom_sdk_manager_path = /path/to/sdkmanager

# (int) Android API level to target
android.api = 34

# (int) Minimum API level required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use Android's default Java 8? (requires Android 8+)
android.use_default_java8 = True

# (str) Python-for-android (p4a) branch to use (default: master)
p4a.branch = develop

# (str) Android package name (must be unique)
android.package_name = org.example.calculator

# (str) Android activity name (must be unique)
android.activity_name = CalculatorActivity

# (str) Presplash background color (Android only)
#android.presplash_color = #FFFFFF

# (str) Presplash image
#android.presplash_image = path/to/presplash.png

# (str) Icon
#android.icon = path/to/icon.png

# (list) Supported orientations
android.orientations = portrait

# (list) Metadata
#android.meta_data = key=value,other=value

# (list) Java libraries to add
#android.add_jars = foo.jar,bar.jar

# (bool) Enable Google Play Services
#android.google_play_services = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) Override the default version of CMake
#android.cmake_version = 3.10.2

# (str) JDK version to use
android.jdk = 17

# (str) Path to the Android SDK
#android.sdk_path = /home/user/android-sdk

# (str) Path to the Android NDK
#android.ndk_path = /home/user/android-ndk

# (str) Path to the Android Ant
#android.ant_path = /usr/share/ant

# (str) Android Gradle plugin version (Android only)
#android.gradle_plugin_version = 4.1.0

# (bool) Enable AndroidX (Android only)
#android.use_androidx = True

# (str) Extra command line arguments for buildozer
#buildozer.extra_args = --enable-crypt

# (bool) Enable the use of TMPDIR for temporary files
#buildozer.tmpdir =

# (str) Log level for buildozer (default: info)
#buildozer.log_level = 2

# (int) Number of parallel build jobs (default: number of CPU cores - 1)
#buildozer.parallel_jobs = 2

# (bool) Use Gradle instead of ant (recommended)
#android.gradle = True

# (str) Path to the Gradle executable
#android.gradle_path = /usr/local/bin/gradle

# (bool) Sign APK? (default: False)
#android.sign_apk = False

# (str) Path to the keystore
#android.keystore = /path/to/keystore

# (str) Keystore password
#android.keyalias =

# (str) Key alias
#android.keystore_password =

# (str) Key password
#android.key_alias_password =

# (list) Additional source dirs (relative to source.dir)
#android.add_src =

# (str) Android app theme
android.app_theme = @android:style/Theme.Material.Light.NoActionBar

# (list) Support libraries to add
#android.support_libs =

# (list) Gradle dependencies
#android.gradle_dependencies =

# (bool) Enable Google Play Billing? (requires google-play-services)
#android.google_play_billing = False

# (bool) Enable Google Play Licensing? (requires google-play-services)
#android.google_play_licensing = False

# (bool) Enable AndroidX? (Android only)
#android.use_androidx = True

# (bool) Enable multidex?
#android.multidex = True

# (int) Minimum SDK version for AndroidX
#android.minimum_sdk_version = 21

# (bool) Enable the use of a Python virtual environment on target device?
#android.use_virtualenv = False

# (str) Path to the virtual environment on target device
#android.virtualenv_path = /data/data/org.example.calculator/files/venv

# (str) The path to the virtual environment on the host
#android.virtualenv_host_path = /path/to/venv

# (str) The path to the Python executable on the host
#android.python_host_path = /usr/bin/python3

# (bool) Enable the use of a compiled Python on target device
#android.compiled_python = True

# (bool) Build the APK in debug mode
#android.debug = True

# (list) Android extra libraries to include (e.g., libcrypto.so)
#android.extra_libs =

# (list) Android extra Java files
#android.extra_java_files =

# (str) Android app theme (for gradle)
#android.app_theme_gradle = @style/AppTheme

# (bool) Enable the use of a custom AndroidManifest.xml
#android.use_custom_manifest = False

# (bool) Enable the use of a custom build.gradle
#android.use_custom_gradle = False

# (bool) Enable the use of a custom build.gradle.kts
#android.use_custom_gradle_kts = False

# (bool) Enable the use of a custom Android.mk
#android.use_custom_mk = False

# (str) Path to the custom AndroidManifest.xml
#android.custom_manifest_path = /path/to/AndroidManifest.xml

# (str) Path to the custom build.gradle
#android.custom_gradle_path = /path/to/build.gradle

# (str) Path to the custom build.gradle.kts
#android.custom_gradle_kts_path = /path/to/build.gradle.kts

# (str) Path to the custom Android.mk
#android.custom_mk_path = /path/to/Android.mk

# (str) The architecture to build for on Android
#android.arch = arm64-v8a

# (bool) Use the latest changes of kivy/python-for-android?
#android.use_latest_p4a = False

# (bool) Enable the use of a custom Android SDK platform (default: False)
#android.use_custom_sdk = False

# (str) Path to the custom Android SDK platform
#android.custom_sdk_path = /path/to/sdk

# (str) Path to the custom Android NDK
#android.custom_ndk_path = /path/to/ndk

# (str) Path to the custom Apache Ant
#android.custom_ant_path = /path/to/ant

# (str) Path to the custom Gradle
#android.custom_gradle_path = /path/to/gradle

# (str) Path to the custom Maven
#android.custom_maven_path = /path/to/maven

# (bool) Enable the use of a custom Maven repository
#android.use_custom_maven_repo = False

# (str) Path to the custom Maven repository
#android.custom_maven_repo_path = /path/to/maven-repo

# (bool) Enable the use of a custom Python-for-android recipe repo
#android.use_custom_p4a_repo = False

# (str) Path to the custom Python-for-android recipe repo
#android.custom_p4a_repo_path = /path/to/p4a-repo

# (list) Additional Python-for-android recipes to include
#android.p4a_recipes =

# (list) Additional Python-for-android patches
#android.p4a_patches =

# (str) The name of the Python-for-android branch to use
#android.p4a_branch = develop

# (str) The Python-for-android commit hash to use
#android.p4a_commit =

# (bool) Enable the use of a custom Python-for-android egg
#android.use_custom_p4a_egg = False

# (str) Path to the custom Python-for-android egg
#android.custom_p4a_egg_path = /path/to/p4a-egg

# (bool) Enable the use of a custom Android virtual device
#android.use_custom_avd = False

# (str) Path to the custom Android virtual device
#android.custom_avd_path = /path/to/avd

# (bool) Enable the use of a custom Android emulator
#android.use_custom_emulator = False

# (str) Path to the custom Android emulator
#android.custom_emulator_path = /path/to/emulator

# (bool) Enable the use of a custom Android device
#android.use_custom_device = False

# (str) Path to the custom Android device
#android.custom_device_path = /path/to/device

# (list) Android extra libraries to include
#android.extra_libs =

# (bool) Enable the use of a custom Android library
#android.use_custom_library = False

# (str) Path to the custom Android library
#android.custom_library_path = /path/to/library

# (list) Android extra Java files
#android.extra_java_files =

# (bool) Enable the use of a custom Java file
#android.use_custom_java = False

# (str) Path to the custom Java file
#android.custom_java_path = /path/to/Java

# (bool) Enable the use of a custom Android resource
#android.use_custom_resource = False

# (str) Path to the custom Android resource
#android.custom_resource_path = /path/to/resource

# (bool) Enable the use of a custom Android asset
#android.use_custom_asset = False

# (str) Path to the custom Android asset
#android.custom_asset_path = /path/to/asset

# (bool) Enable the use of a custom Android library
#android.use_custom_library = False

# (str) Path to the custom Android library
#android.custom_library_path = /path/to/library

# (list) Android extra jars
#android.extra_jars =

# (list) Android extra aars
#android.extra_aars =

# (bool) Enable the use of a custom Android native library
#android.use_custom_native_library = False

# (str) Path to the custom Android native library
#android.custom_native_library_path = /path/to/native

# (bool) Enable the use of a custom Python-for-android recipe
#android.use_custom_p4a_recipe = False

# (str) Path to the custom Python-for-android recipe
#android.custom_p4a_recipe_path = /path/to/p4a-recipe

# (bool) Enable the use of a custom Python-for-android patch
#android.use_custom_p4a_patch = False

# (str) Path to the custom Python-for-android patch
#android.custom_p4a_patch_path = /path/to/p4a-patch

# (bool) Enable the use of a custom Android virtual device
#android.use_custom_avd = False

# (str) Path to the custom Android virtual device
#android.custom_avd_path = /path/to/avd

# (bool) Enable the use of a custom Android emulator
#android.use_custom_emulator = False

# (str) Path to the custom Android emulator
#android.custom_emulator_path = /path/to/emulator

# (bool) Enable the use of a custom Android device
#android.use_custom_device = False

# (str) Path to the custom Android device
#android.custom_device_path = /path/to/device