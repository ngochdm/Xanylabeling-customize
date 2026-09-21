<!-- 
  ____ _   _ ____ _____ ___  __  __ ___ __________ 
 / ___| | | / ___|_   _/ _ \|  \/  |_ _|__  / ____|
| |   | | | \___ \ | || | | | |\/| || |  / /|  _|  
| |___| |_| |___) || || |_| | |  | || | / /_| |___ 
 \____|\___/|____/ |_| \___/|_|  |_|___/____|_____|
                                                   
__  __       _    _   ___   ___        _    ____  _____ _     ___ _   _  ____ 
\ \/ /      / \  | \ | \ \ / / |      / \  | __ )| ____| |   |_ _| \ | |/ ___|
 \  /_____ / _ \ |  \| |\ V /| |     / _ \ |  _ \|  _| | |    | ||  \| | |  _ 
 /  \_____/ ___ \| |\  | | | | |___ / ___ \| |_) | |___| |___ | || |\  | |_| |
/_/\_\   /_/   \_\_| \_| |_| |_____/_/   \_\____/|_____|_____|___|_| \_|\____|

       ____    ____   ___  
__   _|___ \  | ___| / _ \ 
\ \ / / __) | |___ \| | | |
 \ V / / __/ _ ___) | |_| |
  \_/ |_____(_)____(_)___/ 

-->

# 🛠️ Customize X-AnyLabeling v2.5.0 🛠️

This repository is a customized clone of X-AnyLabeling v2.5.0.
- **Original Repo:** https://github.com/CVHub520/X-AnyLabeling/releases/tag/v2.5.0
- Please read [README_Xanylabeling.md](README_Xanylabeling.md) for more detailed information.

**Purpose:**
- Support for manual labeling and evaluating the annotations for long video length (~ 10 minutes).
- Customize bbox visualization for frames containing a number of occluded small objects.


<!-- MARK: ✨ Updates -->

## ✨ Feature Updates

### 📅 Sep 21, 2026 

- Added optional setting label font size.

### Sep 17, 2026

- Added optional setting bounding box thickness.

### July 1, 2026

- Added auto navigation controls in the Files dock.
  - `auto jump` navigates through multiple images automatically.
  - Navigation step count supports forward and backward movement.

- Added LineStrip rotation tools.
  - Rotate selected LineStrip objects left by 90 degrees.
  - Rotate selected LineStrip objects right by 90 degrees.
  - Rotation uses the selected LineStrip bounding center.

- Added custom rotate-left and rotate-right toolbar icons.

- Added `regenerate_icon_ngochdm.sh` for rebuilding updated icon resources.

### June 29, 2026

- Added configurable image navigation interval.
  - `navigation_interval` was added to the config.
  - Previous/next image navigation can jump by more than one image at a time.

### June 24, 2026

- Updated the Files dock default horizontal scroll position.
- Adjusted layout heights for Image/Object Description and Shape dock areas.

### June 23, 2026

- Added and repositioned the zoom bar in the labeling UI.


<!-- MARK: 📝 Notes -->

## 📝 Notes

- This README documents custom changes on top of upstream X-AnyLabeling v2.5.0.
