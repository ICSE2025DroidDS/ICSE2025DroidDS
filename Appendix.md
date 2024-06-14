# Appendix

## Mitigable Cases

This section is intended to provide supporting evidence for  answering Review A's Question 1, Review B's Question 2, and the weakness mentioned in Review C. 

- **Review A#Q1: You discuss the concept of mitigable design smells and provide predicates for identifying them. Have you conducted any practical experiments or case studies to verify whether these mitigable smells can indeed be eradicated as easily as suggested? If not, are there plans to validate these mitigation strategies empirically?**
- **Review B#Q2: Can you remove/rephrase the unsupported claims?**
- **Review C#Weaknesses: The paper makes multiple claims that are not adequately supported by analysis.**

**Concept description**

| Name          | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| Case          | The Case where these design smell instances were eliminated in version history |
| From Entity   | The source entity of relation                                |
| Relation      | The type of relation                                         |
| To Entity     | The destination entity of relation                           |
| Modified Line | The number of modified line to eliminate the design smell    |
| Code Fragment | The real code fragment of Case in Android project            |

We have manually analyzed 73 instances of design smells that were eliminated in the version history, with 24 out of 73 cases identified as mitigable smells. Specifically, the detailed information of the 24 Cases is shown below, including code entities, dependencies, and source code fragment.

### Case 1

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.weatherTileProvider
- **Modified Line : 2**

### Case 2

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.headsupTileProvider
- **Modified Line : 2**

### Case 3

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.powerButtonTileProvider
- **Modified Line : 2**

### Case 4

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.dataSwitchTileProvider
- **Modified Line : 2**

#### Code Fragment in OmniROM-android11 (Case 1 - Case 4)

```java
// packages/SystemUI/src/com/android/systemui/qs/tileimpl/QSFactoryImpl.java
	public QSFactoryImpl(Lazy<QSHost> qsHostLazy,
            Provider<WifiTile> wifiTileProvider,
            Provider<BluetoothTile> bluetoothTileProvider,
            Provider<CellularTile> cellularTileProvider,
            Provider<DndTile> dndTileProvider,
            Provider<ColorInversionTile> colorInversionTileProvider,
            Provider<AirplaneModeTile> airplaneModeTileProvider,
            Provider<WorkModeTile> workModeTileProvider,
            Provider<RotationLockTile> rotationLockTileProvider,
            Provider<FlashlightTile> flashlightTileProvider,
            Provider<LocationTile> locationTileProvider,
            Provider<CastTile> castTileProvider,
            Provider<HotspotTile> hotspotTileProvider,
            Provider<UserTile> userTileProvider,
            Provider<BatterySaverTile> batterySaverTileProvider,
            Provider<DataSaverTile> dataSaverTileProvider,
            Provider<NightDisplayTile> nightDisplayTileProvider,
            Provider<NfcTile> nfcTileProvider,
            Provider<GarbageMonitor.MemoryTile> memoryTileProvider,
            Provider<UiModeNightTile> uiModeNightTileProvider,
            Provider<ScreenRecordTile> screenRecordTileProvider,
            Provider<AODTile> aodTileProvider,
            Provider<WeatherTile> weatherTileProvider, // Case 1
            Provider<HeadsUpTile> headsupTileProvider, // Case 2
            Provider<ScreenshotTile> screenshotTileProvider,
            Provider<PowerButtonTile> powerButtonTileProvider, // Case 3
            Provider<DataSwitchTile> dataSwitchTileProvider) { // Case 4
        mQsHostLazy = qsHostLazy;
        mWifiTileProvider = wifiTileProvider;
        mBluetoothTileProvider = bluetoothTileProvider;
        mCellularTileProvider = cellularTileProvider;
        mDndTileProvider = dndTileProvider;
        mColorInversionTileProvider = colorInversionTileProvider;
        mAirplaneModeTileProvider = airplaneModeTileProvider;
        mWorkModeTileProvider = workModeTileProvider;
        mRotationLockTileProvider = rotationLockTileProvider;
        mFlashlightTileProvider = flashlightTileProvider;
        mLocationTileProvider = locationTileProvider;
        mCastTileProvider = castTileProvider;
        mHotspotTileProvider = hotspotTileProvider;
        mUserTileProvider = userTileProvider;
        mBatterySaverTileProvider = batterySaverTileProvider;
        mDataSaverTileProvider = dataSaverTileProvider;
        mNightDisplayTileProvider = nightDisplayTileProvider;
        mNfcTileProvider = nfcTileProvider;
        mMemoryTileProvider = memoryTileProvider;
        mUiModeNightTileProvider = uiModeNightTileProvider;
        mScreenRecordTileProvider = screenRecordTileProvider;
        //Omni
        mAODTileProvider = aodTileProvider;
        mWeatherTileProvider = weatherTileProvider; // Case 1
        mHeadsUpTileProvider = headsupTileProvider; // Case 2
        mScreenshotTileProvider = screenshotTileProvider; 
        mPowerButtonTileProvider = powerButtonTileProvider; // Case 3
        mDataSwitchTileProvider = dataSwitchTileProvider; // Case 4
    }
```

####  Code Fragment in  OmniROM-android12 (Case 1 - Case 4)

```java
// packages/SystemUI/src/com/android/systemui/qs/tileimpl/QSFactoryImpl.java
	public QSFactoryImpl(
            Lazy<QSHost> qsHostLazy,
            Provider<CustomTile.Builder> customTileBuilderProvider,
            Provider<WifiTile> wifiTileProvider,
            Provider<InternetTile> internetTileProvider,
            Provider<BluetoothTile> bluetoothTileProvider,
            Provider<CellularTile> cellularTileProvider,
            Provider<DndTile> dndTileProvider,
            Provider<ColorInversionTile> colorInversionTileProvider,
            Provider<AirplaneModeTile> airplaneModeTileProvider,
            Provider<WorkModeTile> workModeTileProvider,
            Provider<RotationLockTile> rotationLockTileProvider,
            Provider<FlashlightTile> flashlightTileProvider,
            Provider<LocationTile> locationTileProvider,
            Provider<CastTile> castTileProvider,
            Provider<HotspotTile> hotspotTileProvider,
            Provider<UserTile> userTileProvider,
            Provider<BatterySaverTile> batterySaverTileProvider,
            Provider<DataSaverTile> dataSaverTileProvider,
            Provider<NightDisplayTile> nightDisplayTileProvider,
            Provider<NfcTile> nfcTileProvider,
            Provider<GarbageMonitor.MemoryTile> memoryTileProvider,
            Provider<UiModeNightTile> uiModeNightTileProvider,
            Provider<ScreenRecordTile> screenRecordTileProvider,
            Provider<ReduceBrightColorsTile> reduceBrightColorsTileProvider,
            Provider<CameraToggleTile> cameraToggleTileProvider,
            Provider<MicrophoneToggleTile> microphoneToggleTileProvider,
            Provider<DeviceControlsTile> deviceControlsTileProvider,
            Provider<AlarmTile> alarmTileProvider,
            Provider<QuickAccessWalletTile> quickAccessWalletTileProvider,
            Provider<AODTile> aodTileProvider,
            Provider<ScreenshotTile> screenshotTileProvider,
            Provider<CaffeineTile> caffeineTileProvider) {
        mQsHostLazy = qsHostLazy;
        mCustomTileBuilderProvider = customTileBuilderProvider;

        mWifiTileProvider = wifiTileProvider;
        mInternetTileProvider = internetTileProvider;
        mBluetoothTileProvider = bluetoothTileProvider;
        mCellularTileProvider = cellularTileProvider;
        mDndTileProvider = dndTileProvider;
        mColorInversionTileProvider = colorInversionTileProvider;
        mAirplaneModeTileProvider = airplaneModeTileProvider;
        mWorkModeTileProvider = workModeTileProvider;
        mRotationLockTileProvider = rotationLockTileProvider;
        mFlashlightTileProvider = flashlightTileProvider;
        mLocationTileProvider = locationTileProvider;
        mCastTileProvider = castTileProvider;
        mHotspotTileProvider = hotspotTileProvider;
        mUserTileProvider = userTileProvider;
        mBatterySaverTileProvider = batterySaverTileProvider;
        mDataSaverTileProvider = dataSaverTileProvider;
        mNightDisplayTileProvider = nightDisplayTileProvider;
        mNfcTileProvider = nfcTileProvider;
        mMemoryTileProvider = memoryTileProvider;
        mUiModeNightTileProvider = uiModeNightTileProvider;
        mScreenRecordTileProvider = screenRecordTileProvider;
        mReduceBrightColorsTileProvider = reduceBrightColorsTileProvider;
        mCameraToggleTileProvider = cameraToggleTileProvider;
        mMicrophoneToggleTileProvider = microphoneToggleTileProvider;
        mDeviceControlsTileProvider = deviceControlsTileProvider;
        mAlarmTileProvider = alarmTileProvider;
        mQuickAccessWalletTileProvider = quickAccessWalletTileProvider;

        //Omni
        mAODTileProvider = aodTileProvider;
        mScreenshotTileProvider = screenshotTileProvider;
        mCaffeineTileProvider = caffeineTileProvider;
    }
```

### Case 5

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation: Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.caffeineTileProvider
- **Modified Line : 2**

### Case 6

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.adbOverNetworkProvider
- **Modified Line : 2**

### Case 7

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.scrTileProvider
- **Modified Line : 2**

### Case 8

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.immersiveTileProvider
- **Modified Line : 2**

#### Code Fragment in OmniROM-android10 (Case 5 - Case 8)

```java
// packages/SystemUI/src/com/android/systemui/qs/tileimpl/QSFactoryImpl.java
    public QSFactoryImpl(Provider<WifiTile> wifiTileProvider,
            Provider<BluetoothTile> bluetoothTileProvider,
            Provider<CellularTile> cellularTileProvider,
            Provider<DndTile> dndTileProvider,
            Provider<ColorInversionTile> colorInversionTileProvider,
            Provider<AirplaneModeTile> airplaneModeTileProvider,
            Provider<WorkModeTile> workModeTileProvider,
            Provider<RotationLockTile> rotationLockTileProvider,
            Provider<FlashlightTile> flashlightTileProvider,
            Provider<LocationTile> locationTileProvider,
            Provider<CastTile> castTileProvider,
            Provider<HotspotTile> hotspotTileProvider,
            Provider<UserTile> userTileProvider,
            Provider<BatterySaverTile> batterySaverTileProvider,
            Provider<DataSaverTile> dataSaverTileProvider,
            Provider<NightDisplayTile> nightDisplayTileProvider,
            Provider<NfcTile> nfcTileProvider,
            Provider<GarbageMonitor.MemoryTile> memoryTileProvider,
            Provider<UiModeNightTile> uiModeNightTileProvider,
            Provider<AODTile> aodTileProvider,
            Provider<CaffeineTile> caffeineTileProvider, // Case 5
            Provider<AdbOverNetworkTile> adbOverNetworkProvider, // Case 6
            Provider<ScreenrecordTile> scrTileProvider,  // Case 7
            Provider<WeatherTile> weatherTileProvider,
            Provider<HeadsUpTile> headsupTileProvider,
            Provider<ImmersiveTile> immersiveTileProvider, // Case 8
            Provider<ScreenshotTile> screenshotTileProvider,
            Provider<DataSwitchTile> dataSwitchTileProvider) {
        mWifiTileProvider = wifiTileProvider;
        mBluetoothTileProvider = bluetoothTileProvider;
        mCellularTileProvider = cellularTileProvider;
        mDndTileProvider = dndTileProvider;
        mColorInversionTileProvider = colorInversionTileProvider;
        mAirplaneModeTileProvider = airplaneModeTileProvider;
        mWorkModeTileProvider = workModeTileProvider;
        mRotationLockTileProvider = rotationLockTileProvider;
        mFlashlightTileProvider = flashlightTileProvider;
        mLocationTileProvider = locationTileProvider;
        mCastTileProvider = castTileProvider;
        mHotspotTileProvider = hotspotTileProvider;
        mUserTileProvider = userTileProvider;
        mBatterySaverTileProvider = batterySaverTileProvider;
        mDataSaverTileProvider = dataSaverTileProvider;
        mNightDisplayTileProvider = nightDisplayTileProvider;
        mNfcTileProvider = nfcTileProvider;
        mMemoryTileProvider = memoryTileProvider;
        mUiModeNightTileProvider = uiModeNightTileProvider;
        //Omni
        mAODTileProvider = aodTileProvider;
        mCaffeineTileProvider = caffeineTileProvider; // Case 5
        mAdbOverNetworkProvider = adbOverNetworkProvider; // Case 6
        mScrTileProvider = scrTileProvider;  // Case 7
        mWeatherTileProvider = weatherTileProvider;
        mHeadsUpTileProvider = headsupTileProvider;
        mImmersiveTileProvider = immersiveTileProvider; // Case 8
        mScreenshotTileProvider = screenshotTileProvider;
        mDataSwitchTileProvider = dataSwitchTileProvider;
    }
```



#### Code Fragment in OmniROM-android11 (Case 5 - Case 8)

```java
// packages/SystemUI/src/com/android/systemui/qs/tileimpl/QSFactoryImpl.java
	public QSFactoryImpl(Lazy<QSHost> qsHostLazy,
            Provider<WifiTile> wifiTileProvider,
            Provider<BluetoothTile> bluetoothTileProvider,
            Provider<CellularTile> cellularTileProvider,
            Provider<DndTile> dndTileProvider,
            Provider<ColorInversionTile> colorInversionTileProvider,
            Provider<AirplaneModeTile> airplaneModeTileProvider,
            Provider<WorkModeTile> workModeTileProvider,
            Provider<RotationLockTile> rotationLockTileProvider,
            Provider<FlashlightTile> flashlightTileProvider,
            Provider<LocationTile> locationTileProvider,
            Provider<CastTile> castTileProvider,
            Provider<HotspotTile> hotspotTileProvider,
            Provider<UserTile> userTileProvider,
            Provider<BatterySaverTile> batterySaverTileProvider,
            Provider<DataSaverTile> dataSaverTileProvider,
            Provider<NightDisplayTile> nightDisplayTileProvider,
            Provider<NfcTile> nfcTileProvider,
            Provider<GarbageMonitor.MemoryTile> memoryTileProvider,
            Provider<UiModeNightTile> uiModeNightTileProvider,
            Provider<ScreenRecordTile> screenRecordTileProvider,
            Provider<AODTile> aodTileProvider,
            Provider<WeatherTile> weatherTileProvider,
            Provider<HeadsUpTile> headsupTileProvider,
            Provider<ScreenshotTile> screenshotTileProvider,
            Provider<PowerButtonTile> powerButtonTileProvider,
            Provider<DataSwitchTile> dataSwitchTileProvider) {
        mQsHostLazy = qsHostLazy;
        mWifiTileProvider = wifiTileProvider;
        mBluetoothTileProvider = bluetoothTileProvider;
        mCellularTileProvider = cellularTileProvider;
        mDndTileProvider = dndTileProvider;
        mColorInversionTileProvider = colorInversionTileProvider;
        mAirplaneModeTileProvider = airplaneModeTileProvider;
        mWorkModeTileProvider = workModeTileProvider;
        mRotationLockTileProvider = rotationLockTileProvider;
        mFlashlightTileProvider = flashlightTileProvider;
        mLocationTileProvider = locationTileProvider;
        mCastTileProvider = castTileProvider;
        mHotspotTileProvider = hotspotTileProvider;
        mUserTileProvider = userTileProvider;
        mBatterySaverTileProvider = batterySaverTileProvider;
        mDataSaverTileProvider = dataSaverTileProvider;
        mNightDisplayTileProvider = nightDisplayTileProvider;
        mNfcTileProvider = nfcTileProvider;
        mMemoryTileProvider = memoryTileProvider;
        mUiModeNightTileProvider = uiModeNightTileProvider;
        mScreenRecordTileProvider = screenRecordTileProvider;
        //Omni
        mAODTileProvider = aodTileProvider;
        mWeatherTileProvider = weatherTileProvider;
        mHeadsUpTileProvider = headsupTileProvider;
        mScreenshotTileProvider = screenshotTileProvider; 
        mPowerButtonTileProvider = powerButtonTileProvider;
        mDataSwitchTileProvider = dataSwitchTileProvider;
    }
```

### Case 9

- From Entity : com.android.settingslib.location.SettingsInjector
- Relation : Define
- To Entity : com.android.settingslib.location.SettingsInjector.parseServiceInfo
- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 9)

```java
// services/core/java/com/android/server/wm/ActivityStackSupervisor.java
	protected InjectedSetting parseServiceInfo(ResolveInfo service, UserHandle userHandle, 
            PackageManager pm) throws XmlPullParserException, IOException { 
    	...
    }
```

#### Code Fragment in OmniROM-android12 (Case 9)

```java
// services/core/java/com/android/server/wm/ActivityStackSupervisor.java
	private static InjectedSetting parseServiceInfo(ResolveInfo service, UserHandle userHandle,
            PackageManager pm) throws XmlPullParserException, IOException {
    	...
    }
```

### Case 10

- From Entity : com.android.keyguard.EmergencyButton
- Relation : Define
- To Entity : com.android.keyguard.EmergencyButton.updateEmergencyCallButton

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 10)

```java
// services/core/java/com/android/server/wm/RootWindowContainer.java
	public void updateEmergencyCallButton() {
        boolean visible = false;
        ...
    }
```

#### Code Fragment in OmniROM-android12 (Case 10)

```java
// services/core/java/com/android/server/wm/RootWindowContainer.java
	void updateEmergencyCallButton(boolean isInCall, boolean isVoiceCapable, boolean simLocked) {
        boolean visible = false;
        ...
    }
```

### Case 11

- From Entity : android.telecom.ConnectionService
- Relation : Define
- To Entity : android.telecom.ConnectionService.answerVideo
- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 11)

```java
// telecomm/java/android/telecom/ConnectionService.java
	protected void answerVideo(String callId, int videoState) {
        Log.i(this, "answerVideo %s", callId);
    	...
    }
```

#### Code Fragment in OmniROM-android12 (Case 11)

```java
// telecomm/java/android/telecom/ConnectionService.java
	private void answerVideo(String callId, int videoState) {
        Log.i(this, "answerVideo %s", callId);
        ...
    }
```

### Case 12

- From Entity : android.telecom.ConnectionService
- Relation : Define
- To Entity : android.telecom.ConnectionService.answer
- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 12)

```java
// telecomm/java/android/telecom/ConnectionService.java
	protected void answer(String callId) {
        Log.i(this, "answer %s", callId);
        ...
    }
```

#### Code Fragment in OmniROM-android12 (Case 12)

```java
// telecomm/java/android/telecom/ConnectionService.java	
	private void answer(String callId) {
        Log.i(this, "answer %s", callId);
        ...
    }
```

### Case 13

- From Entity : android.nfc.cardemulation.AidGroup
- Relation : Define
- To Entity : android.nfc.cardemulation.AidGroup.aids

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 13)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    protected List<String> aids;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 13)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    final List<String> aids;
    ...
}
```


### Case 14

- From Entity : android.nfc.cardemulation.AidGroup
- Relation : Define
- To Entity : android.nfc.cardemulation.AidGroup.category

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 14)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    protected String category;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 14)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    final String category;
    ...
}
```


### Case 15

- From Entity : android.nfc.cardemulation.AidGroup
- Relation : Define
- To Entity : android.nfc.cardemulation.AidGroup.description

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 15)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    protected String description;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 15)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    final String description;
    ...
}
```


### Case 16

- From Entity : android.nfc.cardemulation.ApduServiceInfo
- Relation : Define
- To Entity : android.nfc.cardemulation.ApduServiceInfo.mService

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 16)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected ResolveInfo mService;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 16)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final ResolveInfo mService;
    ...
}
```


### Case 17

- From Entity : android.nfc.cardemulation.ApduServiceInfo
- Relation : Define
- To Entity : android.nfc.cardemulation.ApduServiceInfo.mDescription

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 17)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected String mDescription;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 17)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final String mDescription;
    ...
}
```


### Case 18

- From Entity : android.nfc.cardemulation.ApduServiceInfo
- Relation : Define
- To Entity : android.nfc.cardemulation.ApduServiceInfo.mOnHost

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 18)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected boolean mOnHost;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 18)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final boolean mOnHost;
    ...
}
```


### Case 19

- From Entity : android.nfc.cardemulation.ApduServiceInfo
- Relation : Define
- To Entity : android.nfc.cardemulation.ApduServiceInfo.mStaticAidGroups

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 19)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected  HashMap<String, AidGroup> mStaticAidGroups;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 19)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final HashMap<String, AidGroup> mStaticAidGroups;
    ...
}
```


### Case 20

- From Entity : android.nfc.cardemulation.ApduServiceInfo
- Relation : Define
- To Entity : android.nfc.cardemulation.ApduServiceInfo.mDynamicAidGroups

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 20)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected  HashMap<String, AidGroup> mDynamicAidGroups;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 20)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final HashMap<String, AidGroup> mDynamicAidGroups;
    ...
}
```


### Case 21

- From Entity : android.nfc.cardemulation.ApduServiceInfo
- Relation : Define
- To Entity : android.nfc.cardemulation.ApduServiceInfo.mRequiresDeviceUnlock

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 21)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected boolean mRequiresDeviceUnlock;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 21)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final boolean mRequiresDeviceUnlock;
    ...
}
```


### Case 22

- From Entity : android.nfc.cardemulation.ApduServiceInfo
- Relation : Define
- To Entity : android.nfc.cardemulation.ApduServiceInfo.mBannerResourceId

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 22)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected int mBannerResourceId;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 22)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final int mBannerResourceId;
    ...
}
```


### Case 23

- From Entity : android.nfc.cardemulation.ApduServiceInfo
- Relation : Define
- To Entity : android.nfc.cardemulation.ApduServiceInfo.mUid

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 23)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected int mUid;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 23)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final int mUid;
    ...
}
```


### Case 24

- From Entity : android.nfc.cardemulation.ApduServiceInfo
- Relation : Define
- To Entity : android.nfc.cardemulation.ApduServiceInfo.mSettingsActivityName

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 24)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected String mSettingsActivityName;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 24)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final String mSettingsActivityName;
    ...
}
```



## Table 1 Statistics on the number of lines of file code and complexity of files

**Table 1** is intended to provide supporting evidence for  the weakness mentioned in Review C.  It specifies the statistics of LOC (Lines of Code) and Cyclomatic Complexity for 17 versions of 4 projects, categorized by whether files are affected by anti-patterns.

**Review C#Weakness: For example, when analyzing the impact of design smell occurrence on change- and fault-proneness, it is unclear how the authors accounted for confounding factors such as object-oriented smells contained in the files, which are already known to be related to change- and fault-proneness. The authors also did not account for the confounding effects of size and complexity.**

| project   | version      | file_num | aff_num | aff_avg_loc | aff_avg_cc | not_aff_num | not_aff_avg_loc | not_aff_avg_cc |
| --------- | ------------ | -------- | ------- | ----------- | ---------- | ----------- | --------------- | -------------- |
| AOSPA     | quartz       | 9094     | 212     | 2174.797    | 300.8443   | 8882        | 360.7309        | 52.02353       |
| AOSPA     | ruby         | 11947    | 333     | 1684.462    | 215.3393   | 11614       | 355.5857        | 47.84346       |
| AOSPA     | sapphire     | 13524    | 1463    | 994.1661    | 124.028    | 12061       | 313.4398        | 41.46406       |
| AOSPA     | topaz        | 14399    | 329     | 1893.742    | 243.0182   | 14070       | 351.635         | 45.13284       |
| CalyxOS   | android11    | 11957    | 90      | 2310.256    | 361.9556   | 11867       | 377.0133        | 49.98449       |
| CalyxOS   | android12    | 13363    | 75      | 2296.48     | 329.88     | 13288       | 374.7183        | 48.66654       |
| CalyxOS   | android13    | 14326    | 100     | 2330.22     | 329.72     | 14226       | 372.961         | 47.61732       |
| LineageOS | lineage-16.0 | 9107     | 255     | 1666.843    | 254.0078   | 8852        | 366.0451        | 52.12065       |
| LineageOS | lineage-17.1 | 10545    | 270     | 1752.726    | 268.1296   | 10275       | 360.576         | 49.17217       |
| LineageOS | lineage-18.1 | 11969    | 275     | 1690.884    | 233.9091   | 11694       | 361.5008        | 48.11621       |
| LineageOS | lineage-19.1 | 13536    | 263     | 1826.856    | 255.5057   | 13273       | 357.7814        | 46.23084       |
| LineageOS | lineage-20.0 | 14339    | 176     | 1974.92     | 275.1648   | 14163       | 366.9177        | 46.80604       |
| OmniROM   | android-9    | 9107     | 199     | 1938.518    | 266.0603   | 8908        | 367.9894        | 53.05478       |
| OmniROM   | android-10   | 10552    | 247     | 1677.927    | 216.6113   | 10305       | 365.4747        | 50.89044       |
| OmniROM   | android-11   | 12003    | 419     | 1666.203    | 218.4224   | 11584       | 346.2776        | 46.48161       |
| OmniROM   | android-12.0 | 13359    | 100     | 1587.44     | 248.95     | 13259       | 376.5768        | 48.76763       |
| OmniROM   | android-13.0 | 14324    | 96      | 1510.771    | 241.6771   | 14228       | 379.0928        | 48.29667       |

**Concept description for Table 1 columns**

| Name            | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| project         | Andriod project name                                         |
| version         | Detailed version of project                                  |
| file_num        | The number of Java files in the project                      |
| aff_num         | The number of Java files with design smells                  |
| aff_avg_loc     | The average number of line of code in Java files with design smells |
| aff_avg_cc      | The average Cyclomatic Complexity(CC) in Java files with design smells |
| CC              | The sum of Cyclomatic Complexity(CC) of methods in code file |
| not_aff_num     | The number of Java files **without** design smells           |
| not_aff_avg_loc | The average number of line of code in Java files **without** design smells |
| not_aff_avg_cc  | The average Cyclomatic Complexity(CC) in Java files **without** design smells |

## Table 2 The correlation between the occurrence of design code smells in files and the file size as well as code complexity

Based on the data from **Table 1**, we analyzed the correlation between the occurrence of design code smells in files and both file size (measured in Lines of Code, LOC) and code complexity (measured by Cyclomatic Complexity). The strength of these correlations is evaluated using **p-value** and **effect size**.  **Table 2** results indicate a statistically significant and strong correlation between design code smells and both file size and code complexity.

| measure | p-value             | effect size |
| ------- | ------------------- | ----------- |
| LOC     | 7.63E-06 < 0.000001 | 6.09        |
| CC      | 7.63E-06 < 0.000001 | 5.42        |

**Concept description for Table 2 columns**

| Name        | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| measure     | The name of metric                                           |
| p-value     | The p-value is the probability of obtaining results at least as extreme as the observed data, assuming that the null hypothesis is true. |
| effect size | The effect size is a quantitative measure that estimates the magnitude of differences between groups, or strength of relationships between variables. |

## Table 3 The precision and recall of design smells in relation to merge conflicts at the file level

**Table 3** specifies the precision and recall of design smells in relation to merge conflicts at the file level.

| Project | \|ConfF\| | \|ConfF_cap\| | \|CapF\| |  Rec_f  | Precision |
| :-----: | :-------: | :-----------: | :------: | :-----: | :-------: |
|   A-T   |    60     |      40       |   329    | 66.67%  |  12.16%   |
|   A-S   |    183    |      135      |   1463   | 73.77%  |   9.23%   |
|   A-R   |    170    |      110      |   333    | 64.70%  |  33.03%   |
|   A-Q   |    134    |      95       |   212    | 70.90%  |  44.81%   |
|  C-13   |    44     |      22       |   100    | 50.00%  |  22.00%   |
|  C-12   |    18     |       1       |    75    |  5.56%  |   1.33%   |
|  C-11   |     1     |       1       |    90    |  100%   |   1.11%   |
| L-20.0  |    77     |      52       |   176    | 67.53%  |  29.55%   |
| L-19.1  |     2     |       2       |   263    | 100.00% |   0.76%   |
| L-18.1  |    18     |      10       |   275    | 55.56%  |   3.64%   |
| L-17.1  |    43     |      21       |   270    | 53.49%  |   7.78%   |
| L-16.0  |    23     |      16       |   255    | 69.57%  |   6.27%   |
| O-13.0  |    42     |      26       |    96    | 61.90%  |  27.08%   |
| O-12.0  |     9     |       2       |   100    | 22.22%  |   2.00%   |
|  O-11   |    255    |      147      |   419    | 58.43%  |  35.08%   |
|  O-10   |    36     |      26       |   247    | 72.22%  |  10.53%   |
|   O-9   |    10     |       7       |   199    | 70.00%  |   3.52%   |
|   I-E   |    534    |      485      |   2146   | 90.82%  |  22.60%   |
|   I-D   |    534    |      502      |   2308   | 94.01%  |  21.75%   |
|   I-C   |    534    |      502      |   2246   | 94.01%  |  22.35%   |
|   I-B   |    500    |      454      |   2221   | 90.80%  |  20.44%   |
|   I-A   |    321    |      266      |   1817   | 82.87%  |  14.64%   |
| Average |    161    |      133      |   711    | 68.62%  |  15.98%   |

## Table 4 The recall of design smells in relation to merge conflicts at the block level

**Table 4** specifies the recall of design smells in relation to merge conflicts at the block level.

| Project | \|ConfB\| | \|ConfB_cap\| |  Rec_b  |
| :-----: | :-------: | :-----------: | :-----: |
|   A-T   |    140    |      78       | 55.71%  |
|   A-S   |    677    |      509      | 75.18%  |
|   A-R   |    710    |      555      | 78.17%  |
|   A-Q   |    479    |      362      | 75.57%  |
|  C-13   |    95     |      74       | 77.89%  |
|  C-12   |    57     |       1       |  1.75%  |
|  C-11   |     1     |       1       | 100.00% |
| L-20.0  |    190    |      128      | 67.37%  |
| L-19.1  |     5     |       5       | 100.00% |
| L-18.1  |    32     |      15       | 46.88%  |
| L-17.1  |    97     |      56       | 57.73%  |
| L-16.0  |    37     |      29       | 78.38%  |
| O-13.0  |    111    |      56       | 50.45%  |
| O-12.0  |    15     |       4       | 26.67%  |
|  O-11   |   1311    |      972      | 74.14%  |
|  O-10   |    65     |      47       | 72.31%  |
|   O-9   |    16     |      12       | 75.00%  |
|   I-E   |   2359    |     2261      | 95.85%  |
|   I-D   |   2359    |     2304      | 97.67%  |
|   I-C   |   2359    |     2304      | 97.67%  |
|   I-B   |   2846    |     2754      | 96.77%  |
|   I-A   |   1322    |     1170      | 88.50%  |
| Average |    695    |      623      | 72.76%  |

## Table 5 Statistical analysis of conflict blocks associated with design smells and non-design-smells files

|   Measure    | p-value | effect size |
| :----------: | :-----: | :---------: |
| conf_average |  0.002  |    0.974    |

## Table 6 Validation results of recurring conflict blocks across commits

| Project | **Block** | **Text-50%** | **Manual** | Recall | Precision |
| :-----: | :-------: | :----------: | :--------: | :----: | :-------: |
|   A-T   |    140    |      0       |     0      |   0    |     0     |
|   A-S   |    261    |      10      |     12     | 83.33% |   100%    |
|   A-R   |    202    |      12      |     10     |  100%  |  83.33%   |
|   A-Q   |    216    |      8       |     10     |  80%   |   100%    |
|  C-13   |    95     |      0       |     0      |   0    |     0     |
|  C-12   |    47     |      0       |     0      |   0    |     0     |
|  C-11   |     1     |      0       |     0      |   0    |     0     |
| L-20.0  |    190    |      0       |     4      |   0    |     0     |
| L-19.1  |     5     |      0       |     0      |   0    |     0     |
| L-18.1  |    31     |      4       |     4      |  100%  |   100%    |
| L-17.1  |    95     |      11      |     12     | 91.67% |   100%    |
| O-13.0  |    111    |      6       |     6      |  100%  |   100%    |
| O-12.0  |    15     |      0       |     0      |   0    |     0     |
|  O-11   |    426    |      61      |     26     |  100%  |  42.62%   |
|  O-10   |    59     |      0       |     0      |   0    |     0     |
|   O-9   |    12     |      0       |     0      |   0    |     0     |
| Average |    119    |      7       |     5      | 40.94% |  39.12%   |

## Table 7 Validation results of recurring conflict blocks across versions

|  Project  | **Block** | **Text-50%** | **Manual** | Recall | Precision |
| :-------: | :-------: | :----------: | :--------: | :----: | :-------: |
|   AOSPA   |    819    |      35      |     37     | 94.59% |   100%    |
|  CalyxOS  |    143    |      0       |     0      |   0    |     0     |
| LineageOS |    321    |      9       |     9      |  100%  |   100%    |
|  OmniROM  |    623    |      4       |     4      |  100%  |   100%    |
|  Average  |    477    |      12      |     13     | 74.65% |  75.00%   |

## Table 8 Validation results of recurring conflict blocks across projects

| **Project**  | **Block** | **Text-50%** | **Manual** | Recall | Precision |
| :----------: | :-------: | :----------: | :--------: | :----: | :-------: |
| Diff-project |   1906    |     672      |    648     |  100%  |  96.43%   |

