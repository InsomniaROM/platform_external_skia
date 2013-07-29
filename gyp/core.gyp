# Core Skia library code.
{
  'targets': [
    {
      'target_name': 'core',
      'product_name': 'skia_core',
      'type': 'static_library',
      'standalone_static_library': 1,
      'msvs_guid': 'B7760B5E-BFA8-486B-ACFD-49E3A6DE8E76',

      'includes': [
        'core.gypi',
      ],

      'include_dirs': [
        '../include/config',
        '../include/core',
        '../include/pipe',
        '../include/ports',
        '../include/utils',
        '../include/xml',
        '../src/core',
        '../src/image',
      ],
      'sources': [
        'core.gypi', # Makes the gypi appear in IDEs (but does not modify the build).
      ],
      'msvs_disabled_warnings': [4244, 4267,4345, 4390, 4554, 4800],
      'conditions': [
        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
          'cflags': [
            '-Wno-unused',
            '-Wno-unused-function',
          ],
          'link_settings': {
            'libraries': [
              '-lpthread',
            ],
          },
        }],
        [ 'skia_os == "mac"', {
          'include_dirs': [
            '../include/utils/mac',
            '../third_party/freetype/include/**',
          ],
          'sources': [
            '../include/utils/mac/SkCGUtils.h',
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework',
            ],
          },
        }],
        [ 'skia_os == "ios"', {
          'include_dirs': [
            '../include/utils/ios',
          ],
          'sources': [
            '../include/utils/mac/SkCGUtils.h',
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/CoreFoundation.framework',
              '$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
              '$(SDKROOT)/System/Library/Frameworks/CoreText.framework',
              '$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
              '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
              '$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
              '$(SDKROOT)/System/Library/Frameworks/OpenGLES.framework',
              '$(SDKROOT)/System/Library/Frameworks/ImageIO.framework',
              '$(SDKROOT)/System/Library/Frameworks/MobileCoreServices.framework',
            ],
          },
        }],
        [ 'skia_os == "win"', {
          'include_dirs': [
            'config/win',
          ],
          'sources!': [
            '../include/core/SkMMapStream.h',
            '../src/core/SkMMapStream.cpp',
          ],
        }],
        [ 'skia_os == "android"', {
          'dependencies': [
             'freetype.gyp:freetype',
          ],
        }],
        [ 'skia_os == "android" and skia_arch_type == "arm" and armv7 == 1', {
          # The code in SkUtilsArm.cpp can be used on an ARM-based Linux system, not only Android.
          'sources': [
            '../src/core/SkUtilsArm.cpp',
            '../src/core/SkUtilsArm.h',
          ],
        }],
        ['skia_gpu == 1', {
          'include_dirs': [
              '../include/gpu',
              '../src/gpu',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'config',
          '../include/config',
          '../include/core',
          '../include/pipe',
          'ext',
        ],
        'conditions': [
          [ 'skia_os == "mac"', {
            'include_dirs': [
              '../include/utils/mac',
              '../third_party/freetype/include/**',
            ],
          }],
          [ 'skia_os == "ios"', {
            'include_dirs': [
              '../include/utils/ios',
            ],
          }],
          [ 'skia_os == "win"', {
            'include_dirs': [
              'config/win',
            ],
          }],
        ],
      },
      'dependencies': [
        'opts.gyp:opts'
      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
