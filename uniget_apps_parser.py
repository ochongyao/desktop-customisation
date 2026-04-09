import json

# Sample JSON data (replace this with your actual JSON data or load from a file)
data = {
  "export_version": 3,
  "packages": [
    {
      "Id": "7zip.7zip",
      "Name": "7-Zip",
      "Version": "26.00",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Anaconda.Miniconda3",
      "Name": "Miniconda3",
      "Version": "py313_25.11.1-1",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "AntibodySoftware.WizTree",
      "Name": "WizTree",
      "Version": "4.30",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "AnyDesk.AnyDesk",
      "Name": "AnyDesk",
      "Version": "ad 9.6.11",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "CPUID.HWMonitor",
      "Name": "CPUID HWMonitor",
      "Version": "1.62",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "DupeGuru.DupeGuru",
      "Name": "dupeGuru",
      "Version": "4.3.1",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Git.Git",
      "Name": "Git",
      "Version": "2.53.0.2",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "GitHub.GitHubDesktop",
      "Name": "GitHub Desktop",
      "Version": "3.5.6",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "GitHub.GitLFS",
      "Name": "Git LFS",
      "Version": "3.7.1",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Google.Chrome.EXE",
      "Name": "Google Chrome (EXE)",
      "Version": "146.0.7680.80",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Google.QuickShare",
      "Name": "Quick Share from Google",
      "Version": "1.0.2472.1",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "IrfanSkiljan.IrfanView",
      "Name": "IrfanView",
      "Version": "4.73",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "KDE.Kdenlive",
      "Name": "Kdenlive",
      "Version": "25.12.3",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.AppInstaller",
      "Name": "App Installer",
      "Version": "1.28.220.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.DirectX",
      "Name": "DirectX End-User Runtime Installer",
      "Version": "9.29.1974.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.DotNet.AspNetCore.8",
      "Name": "Microsoft ASP.NET Core Runtime 8.0",
      "Version": "8.0.25",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.DotNet.DesktopRuntime.6",
      "Name": "Microsoft .NET Windows Desktop Runtime 6.0",
      "Version": "6.0.36",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.DotNet.DesktopRuntime.8",
      "Name": "Microsoft .NET Windows Desktop Runtime 8.0",
      "Version": "8.0.25",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.DotNet.DesktopRuntime.9",
      "Name": "Microsoft .NET Windows Desktop Runtime 9.0",
      "Version": "9.0.14",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.DotNet.Runtime.8",
      "Name": "Microsoft .NET Runtime 8.0",
      "Version": "8.0.25",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.Edge",
      "Name": "Microsoft Edge",
      "Version": "146.0.3856.62",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.GameInput",
      "Name": "Microsoft GameInput",
      "Version": "10.1.26100.6879",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.OneDrive",
      "Name": "Microsoft OneDrive",
      "Version": "26.032.0217.0003",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.UI.Xaml.2.7",
      "Name": "Microsoft.UI.Xaml",
      "Version": "7.2409.9001.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.UI.Xaml.2.8",
      "Name": "Microsoft.UI.Xaml",
      "Version": "8.2501.31001.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.VCLibs.14",
      "Name": "Microsoft Visual C\u002B\u002B 2015 UWP Runtime Package",
      "Version": "14.0.33519.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.VCLibs.Desktop.14",
      "Name": "Microsoft Visual C\u002B\u002B 2015 UWP Desktop Runtime Package",
      "Version": "14.0.33728.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.VCRedist.2008.x64",
      "Name": "Microsoft Visual C\u002B\u002B 2008 Redistributable - x64",
      "Version": "9.0.30729.6161",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.VCRedist.2008.x86",
      "Name": "Microsoft Visual C\u002B\u002B 2008 Redistributable - x86",
      "Version": "9.0.30729.6161",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.VCRedist.2015\u002B.x64",
      "Name": "Microsoft Visual C\u002B\u002B v14 Redistributable (x64)",
      "Version": "14.50.35719.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.VCRedist.2015\u002B.x86",
      "Name": "Microsoft Visual C\u002B\u002B v14 Redistributable (x86)",
      "Version": "14.44.35211.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.WSL",
      "Name": "Windows Subsystem for Linux",
      "Version": "2.6.3.0",
      "Source": "winget",
      "ManagerName": "Winget",
      "Updates": {
        "IgnoredVersion": "2.4.13.0"
      }
    },
    {
      "Id": "Microsoft.WindowsAppRuntime.1.8",
      "Name": "Windows App Runtime 1.8",
      "Version": "1.8.5",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Microsoft.WindowsTerminal",
      "Name": "Windows Terminal",
      "Version": "1.24.10621.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Nikkho.FileOptimizer",
      "Name": "FileOptimizer",
      "Version": "17.1.0.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Nvidia.CUDA",
      "Name": "NVIDIA CUDA Toolkit",
      "Version": "13.0",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Nvidia.PhysX",
      "Name": "NVIDIA PhysX System Software",
      "Version": "9.23.1019",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "OpenJS.NodeJS.22",
      "Name": "Node.js 22",
      "Version": "22.22.0",
      "Source": "winget",
      "ManagerName": "Winget",
      "Updates": {
        "IgnoredVersion": "22.16.0"
      }
    },
    {
      "Id": "PDFgear.PDFgear",
      "Name": "PDFgear",
      "Version": "2.1.14",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "Ultimaker.Cura",
      "Name": "Ultimaker Cura",
      "Version": "5.12.0",
      "Source": "winget",
      "ManagerName": "Winget",
      "Updates": {
        "IgnoredVersion": "5.10.1"
      }
    },
    {
      "Id": "XP9KHM4BK9FZ7Q",
      "Name": "Visual Studio Code",
      "Version": "\u003E 1.83.1",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "XPDC2RH70K22MN",
      "Name": "Discord",
      "Version": "1.0.9228",
      "Source": "msstore",
      "ManagerName": "Winget"
    },
    {
      "Id": "XPDM1ZW6815MQM",
      "Name": "VLC",
      "Version": "3.0.23",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "XPFFH613W8V6LV",
      "Name": "OBS Studio",
      "Version": "32.0.4",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "XPFFTQ032PTPHF",
      "Name": "UniGetUI",
      "Version": "3.3.7",
      "Source": "msstore",
      "ManagerName": "Winget"
    },
    {
      "Id": "Zoom.Zoom.EXE",
      "Name": "Zoom Workplace (EXE)",
      "Version": "6.7.8 (32670)",
      "Source": "winget",
      "ManagerName": "Winget",
      "Updates": {
        "IgnoredVersion": "6.6.6 (19875)"
      }
    },
    {
      "Id": "glzr-io.glazewm",
      "Name": "GlazeWM",
      "Version": "3.9.1",
      "Source": "winget",
      "ManagerName": "Winget"
    },
    {
      "Id": "nilesoft-shell",
      "Name": "Nilesoft Shell",
      "Version": "1.9.18",
      "Source": "extras",
      "ManagerName": "Scoop"
    },
    {
      "Id": "scoop-search",
      "Name": "Scoop Search",
      "Version": "2.1.0",
      "Source": "main",
      "ManagerName": "Scoop"
    }
  ],
  "incompatible_packages_info": "Incompatible packages cannot be installed from UniGetUI, either because they came from a local source (for example Local PC) or because the package manager was unavailable. Nevertheless, they have been listed here for logging purposes.",
  "incompatible_packages": [
    {
      "Id": "ARP\\Machine\\X64\\Everything",
      "Name": "Everything 1.4.1.1032 (x64)",
      "Version": "1.4.1.1032",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X64\\Intel(R) Graphics Software \u0026 Drivers",
      "Name": "Intel(R) Graphics Software \u0026 Drivers",
      "Version": "1.0.1133.5",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X64\\O365HomePremRetail - en-us",
      "Name": "Microsoft 365 - en-us",
      "Version": "16.0.19725.20172",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X64\\OneNoteFreeRetail - en-us",
      "Name": "Microsoft OneNote - en-us",
      "Version": "16.0.19725.20172",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X64\\RawTherapee5.12_is1",
      "Name": "RawTherapee version 5.12",
      "Version": "5.12",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X64\\c7cfa51a-8bd9-57ef-a77d-3259ad08b8ca",
      "Name": "ATK HUB3.1.0",
      "Version": "3.1.0",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X64\\{2BA535F4-FEF9-45E1-9FF6-66C4E0F629FF}",
      "Name": "oneAPI Level Zero",
      "Version": "1.24.0",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X64\\{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}_Display.Driver",
      "Name": "NVIDIA Graphics Driver 591.74",
      "Version": "591.74",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X64\\{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}_HDAudio.Driver",
      "Name": "NVIDIA HD Audio Driver 1.4.5.7",
      "Version": "1.4.5.7",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X86\\{1851460E-0E63-4117-B5BA-25A2F045801B}",
      "Name": "vs_CoreEditorFonts",
      "Version": "17.7.40001",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X86\\{212860F4-C588-4A41-90A2-B4A2B11D6223}_is1",
      "Name": "AULA F75",
      "Version": "2.0",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\Machine\\X86\\{E63F47A7-9DBA-4154-A52F-36653BFB4028}",
      "Name": "Windows SDK AddOn",
      "Version": "10.1.0.0",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\User\\X64\\459fc68c-eb53-59f8-8957-9913bc627af3",
      "Name": "Arduino IDE 2.3.6",
      "Version": "2.3.6",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\User\\X64\\Jan",
      "Name": "Jan",
      "Version": "0.7.7",
      "Source": "Local PC"
    },
    {
      "Id": "ARP\\User\\X64\\{98c416c8-ccda-48dc-9070-acba7c8993f9}",
      "Name": "MSYS2",
      "Version": "20241208",
      "Source": "Local PC"
    },
    {
      "Id": "MSIX\\AppleInc.AppleMusicWin_1.1538.24068.0_x64__nzyj5cx40ttqa",
      "Name": "Apple Music",
      "Version": "1.1538.24068.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\AppleInc.AppleTVWin_1.1538.24068.0_x64__nzyj5cx40ttqa",
      "Name": "Apple TV",
      "Version": "1.1538.24068.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.AV1VideoExtension_2.0.7.0_x64__8wekyb3d8bbwe",
      "Name": "AV1 Video Extension",
      "Version": "2.0.7.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.AVCEncoderVideoExtension_1.1.23.0_x64__8wekyb3d8bbwe",
      "Name": "AVC Encoder Video Extension",
      "Version": "1.1.23.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.ApplicationCompatibilityEnhancements_1.2511.9.0_x64__8wekyb3d8bbwe",
      "Name": "Windows Application Compatibility Enhancements",
      "Version": "1.2511.9.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.HEIFImageExtension_1.2.29.0_x64__8wekyb3d8bbwe",
      "Name": "HEIF Image Extension",
      "Version": "1.2.29.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.LanguageExperiencePacken-US_26100.128.141.0_neutral__8wekyb3d8bbwe",
      "Name": "English (United States) Local Experience Pack",
      "Version": "26100.128.141.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.MPEG2VideoExtension_1.2.13.0_x64__8wekyb3d8bbwe",
      "Name": "MPEG-2 Video Extension",
      "Version": "1.2.13.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.MicrosoftEdge.Stable_145.0.3800.97_neutral__8wekyb3d8bbwe",
      "Name": "Microsoft Edge",
      "Version": "145.0.3800.97",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.MicrosoftStickyNotes_6.1.4.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft Sticky Notes",
      "Version": "6.1.4.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.NET.Native.Framework.1.3_1.3.24211.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft .Net Native Framework Package 1.3",
      "Version": "1.3.24211.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.NET.Native.Framework.1.3_1.3.24211.0_x86__8wekyb3d8bbwe",
      "Name": "Microsoft .Net Native Framework Package 1.3",
      "Version": "1.3.24211.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.NET.Native.Framework.2.2_2.2.29512.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft .Net Native Framework Package 2.2",
      "Version": "2.2.29512.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.NET.Native.Framework.2.2_2.2.29512.0_x86__8wekyb3d8bbwe",
      "Name": "Microsoft .Net Native Framework Package 2.2",
      "Version": "2.2.29512.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.NET.Native.Runtime.1.4_1.4.24201.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft .Net Native Runtime Package 1.4",
      "Version": "1.4.24201.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.NET.Native.Runtime.1.4_1.4.24201.0_x86__8wekyb3d8bbwe",
      "Name": "Microsoft .Net Native Runtime Package 1.4",
      "Version": "1.4.24201.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.NET.Native.Runtime.2.2_2.2.28604.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft .Net Native Runtime Package 2.2",
      "Version": "2.2.28604.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.NET.Native.Runtime.2.2_2.2.28604.0_x86__8wekyb3d8bbwe",
      "Name": "Microsoft .Net Native Runtime Package 2.2",
      "Version": "2.2.28604.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.Office.ActionsServer_16.0.19725.20172_neutral__8wekyb3d8bbwe",
      "Name": "Microsoft.Office.ActionsServer",
      "Version": "16.0.19725.20172",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.Office.OneNoteVirtualPrinter_1.0.0.0_x64__8wekyb3d8bbwe",
      "Name": "OneNote Virtual Printer",
      "Version": "1.0.0.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.OfficePushNotificationUtility_16.0.19725.20172_neutral__8wekyb3d8bbwe",
      "Name": "OfficePushNotificationsUtility",
      "Version": "16.0.19725.20172",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.OneDriveSync_26032.217.3.0_neutral__8wekyb3d8bbwe",
      "Name": "OneDrive",
      "Version": "26032.217.3.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.Paint_11.2601.401.0_x64__8wekyb3d8bbwe",
      "Name": "Paint",
      "Version": "11.2601.401.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.RawImageExtension_2.5.7.0_x64__8wekyb3d8bbwe",
      "Name": "Raw Image Extension",
      "Version": "2.5.7.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.ScreenSketch_11.2601.0.0_x64__8wekyb3d8bbwe",
      "Name": "Snipping Tool",
      "Version": "11.2601.0.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.SecHealthUI_1000.29510.1001.0_x64__8wekyb3d8bbwe",
      "Name": "Windows Security",
      "Version": "1000.29510.1001.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.Services.Store.Engagement_10.0.23012.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft Engagement Framework",
      "Version": "10.0.23012.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.Services.Store.Engagement_10.0.23012.0_x86__8wekyb3d8bbwe",
      "Name": "Microsoft Engagement Framework",
      "Version": "10.0.23012.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.StorePurchaseApp_22512.1401.1.0_x64__8wekyb3d8bbwe",
      "Name": "Store Experience Host",
      "Version": "22512.1401.1.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.VCLibs.110.00.UWPDesktop_11.0.61135.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft Visual C\u002B\u002B 2012 UWP Desktop Runtime Package",
      "Version": "11.0.61135.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.VCLibs.110.00.UWPDesktop_11.0.61135.0_x86__8wekyb3d8bbwe",
      "Name": "Microsoft Visual C\u002B\u002B 2012 UWP Desktop Runtime Package",
      "Version": "11.0.61135.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.VCLibs.120.00.UWPDesktop_12.0.40653.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft Visual C\u002B\u002B 2013 UWP Desktop Runtime Package",
      "Version": "12.0.40653.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.VCLibs.120.00.UWPDesktop_12.0.40653.0_x86__8wekyb3d8bbwe",
      "Name": "Microsoft Visual C\u002B\u002B 2013 UWP Desktop Runtime Package",
      "Version": "12.0.40653.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.VP9VideoExtensions_1.2.12.0_x64__8wekyb3d8bbwe",
      "Name": "VP9 Video Extensions",
      "Version": "1.2.12.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.VisualStudioCode_1.0.111.0_neutral__8wekyb3d8bbwe",
      "Name": "Visual Studio Code",
      "Version": "1.0.111.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WebMediaExtensions_1.2.17.0_x64__8wekyb3d8bbwe",
      "Name": "Web Media Extensions",
      "Version": "1.2.17.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WebpImageExtension_1.2.14.0_x64__8wekyb3d8bbwe",
      "Name": "WebP Image Extension",
      "Version": "1.2.14.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WinAppRuntime.DDLM.8000.770.947.0-x6_8000.770.947.0_x64__8wekyb3d8bbwe",
      "Name": "Windows App Runtime DDLM 8000.770.947.0-x6",
      "Version": "8000.770.947.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.Windows.DevHome_0.2101.858.0_x64__8wekyb3d8bbwe",
      "Name": "Windows Advanced Settings",
      "Version": "0.2101.858.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.Windows.Photos_2026.11020.20001.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft Photos",
      "Version": "2026.11020.20001.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAlarms_11.2512.0.0_x64__8wekyb3d8bbwe",
      "Name": "Windows Clock",
      "Version": "11.2512.0.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.1_1005.616.1651.0_x64__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.1",
      "Version": "1005.616.1651.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.1_1005.616.1651.0_x86__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.1",
      "Version": "1005.616.1651.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.3_3000.934.1904.0_x64__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.3",
      "Version": "3000.934.1904.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.3_3000.934.1904.0_x86__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.3",
      "Version": "3000.934.1904.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.4_4000.1309.2056.0_x64__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.4",
      "Version": "4000.1309.2056.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.4_4000.1309.2056.0_x86__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.4",
      "Version": "4000.1309.2056.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.5_5001.373.1736.0_x64__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.5",
      "Version": "5001.373.1736.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.5_5001.373.1736.0_x86__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.5",
      "Version": "5001.373.1736.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.6_6000.519.329.0_x64__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.6",
      "Version": "6000.519.329.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.6_6000.519.329.0_x86__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.6",
      "Version": "6000.519.329.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.7_7000.770.750.0_x64__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.7",
      "Version": "7000.770.750.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.7_7000.785.2325.0_x64__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.7",
      "Version": "7000.785.2325.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsAppRuntime.1.7_7000.785.2325.0_x86__8wekyb3d8bbwe",
      "Name": "WindowsAppRuntime.1.7",
      "Version": "7000.785.2325.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsCalculator_11.2508.4.0_x64__8wekyb3d8bbwe",
      "Name": "Windows Calculator",
      "Version": "11.2508.4.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsCamera_2025.2510.2.0_x64__8wekyb3d8bbwe",
      "Name": "Windows Camera",
      "Version": "2025.2510.2.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsNotepad_11.2512.26.0_x64__8wekyb3d8bbwe",
      "Name": "Windows Notepad",
      "Version": "11.2512.26.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsSoundRecorder_1.1.86.0_x64__8wekyb3d8bbwe",
      "Name": "Windows Sound Recorder",
      "Version": "1.1.86.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.WindowsStore_22602.1401.3.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft Store",
      "Version": "22602.1401.3.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.Winget.Fonts.Source_2025.1016.311.49_neutral__8wekyb3d8bbwe",
      "Name": "Windows Package Manager Source (winget-font) V2",
      "Version": "2025.1016.311.49",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.Winget.Source_2026.318.1312.29_neutral__8wekyb3d8bbwe",
      "Name": "Windows Package Manager Source (winget) V2",
      "Version": "2026.318.1312.29",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\Microsoft.XboxGamingOverlay_7.326.2102.0_x64__8wekyb3d8bbwe",
      "Name": "Game Bar",
      "Version": "7.326.2102.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftCorporationII.MicrosoftFamily_0.2.40.0_x64__8wekyb3d8bbwe",
      "Name": "Microsoft Family",
      "Version": "0.2.40.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftCorporationII.WinAppRuntime.Main.1.5_5001.373.1736.0_x64__8wekyb3d8bbwe",
      "Name": "WinAppRuntime.Main.1.5",
      "Version": "5001.373.1736.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftCorporationII.WinAppRuntime.Main.1.8_8000.770.947.0_x64__8wekyb3d8bbwe",
      "Name": "WinAppRuntime.Main.1.8",
      "Version": "8000.770.947.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftCorporationII.WinAppRuntime.Singleton_8000.770.947.0_x64__8wekyb3d8bbwe",
      "Name": "WinAppRuntime.Singleton",
      "Version": "8000.770.947.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftWindows.NarratorScript.Excel_1.0.14.0_neutral__cw5n1h2txyewy",
      "Name": "Narrator Extension - Excel",
      "Version": "1.0.14.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftWindows.NarratorScript.Outlook_1.0.8.0_neutral__cw5n1h2txyewy",
      "Name": "NarratorExtension - Outlook",
      "Version": "1.0.8.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftWindows.Speech.en-GB.1_1.0.14.0_x64__cw5n1h2txyewy",
      "Name": "Speech Pack - English (United Kingdom)",
      "Version": "1.0.14.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftWindows.Speech.en-US.1_1.0.24.0_x64__cw5n1h2txyewy",
      "Name": "Speech Pack - English (United States)",
      "Version": "1.0.24.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftWindows.Speech.zh-CN.1_1.0.22.0_x64__cw5n1h2txyewy",
      "Name": "Speech Pack - Chinese (Simplified)",
      "Version": "1.0.22.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftWindows.Voice.en-GB.Sonia.1_1.0.4.0_x64__cw5n1h2txyewy",
      "Name": "Microsoft Sonia (Natural) - English (United Kingdom)",
      "Version": "1.0.4.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftWindows.Voice.en-US.Jenny.1_1.0.8.0_x64__cw5n1h2txyewy",
      "Name": "Microsoft Jenny (Natural) - English (United States)",
      "Version": "1.0.8.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\MicrosoftWindows.Voice.zh-CN.Yunxi.1_1.0.5.0_x64__cw5n1h2txyewy",
      "Name": "Microsoft Yunxi (Natural) - Chinese (Simplified, China)",
      "Version": "1.0.5.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\NVIDIACorp.NVIDIAControlPanel_8.1.969.0_x64__56jybvy8sckqj",
      "Name": "NVIDIA Control Panel",
      "Version": "8.1.969.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\VisualComputingLab-ISTI-C.MeshLab_2025.7.0.0_x64__c8c2mafe4x7s8",
      "Name": "MeshLab",
      "Version": "2025.7.0.0",
      "Source": "Microsoft Store"
    },
    {
      "Id": "MSIX\\aimgr_0.20.42.0_x64__8wekyb3d8bbwe",
      "Name": "Local AI Manager for Microsoft 365",
      "Version": "0.20.42.0",
      "Source": "Microsoft Store"
    }
  ]
}

# Extract app names from packages
package_names = [package["Name"] for package in data.get("packages", [])]

# Extract app names from incompatible_packages
incompatible_package_names = [package["Name"] for package in data.get("incompatible_packages", [])]

# Combine both lists
all_app_names = package_names + incompatible_package_names

# Print the list of app names
for name in all_app_names:
    print(name)
