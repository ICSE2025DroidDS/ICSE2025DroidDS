# Appendix

## Mitigable Cases

**Q:You discuss the concept of mitigable design smells and provide predicates for identifying them. Have you conducted any practical experiments or case studies to verify whether these mitigable smells can indeed be eradicated as easily as suggested? If not, are there plans to validate these mitigation strategies empirically?**

**Concept Description:**

| Name          | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| Case$         | The Case where these design smell instances were refactored in version history |
| From Entity   | The source entity of relation                                |
| Relation      | The type of relation                                         |
| To Entity     | The destination entity of relation                           |
| modified line | The number of modified line to refactor the design smell     |
| Code fragment | The real code fragment of $Case$ in Android project          |

We have manually analyzed 73 instances of design smells that were eliminated in the version history, with 24 out of 73 cases identified as mitigable smells. The detailed information of 24 Cases are shown as below: 

### Case 1

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.weatherTileProvider
- **modified line : 2**

### Case 2

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.headsupTileProvider
- **modified line : 2**

### Case 3

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.powerButtonTileProvider
- **modified line : 2**

### Case 4

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.dataSwitchTileProvider
- **modified line : 2**

#### Code fragment in OmniROM-android11 (Case 1 - Case 4)

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

####  Code fragment in  OmniROM-android12 (Case 1 - Case 4)

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
- **modified line : 2**

### Case 6

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.adbOverNetworkProvider
- **modified line : 2**

### Case 7

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.scrTileProvider
- **modified line : 2**

### Case 8

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.immersiveTileProvider
- **modified line : 2**

#### Code fragment in OmniROM-android10 (Case 5 - Case 8)

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



#### Code fragment in OmniROM-android11 (Case 5 - Case 8)

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
- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 9)

```java
    protected InjectedSetting parseServiceInfo(ResolveInfo service, UserHandle userHandle, 
            PackageManager pm) throws XmlPullParserException, IOException { 
    	...
    }
```

#### Code fragment in OmniROM-android12 (Case 9)

```java
    private static InjectedSetting parseServiceInfo(ResolveInfo service, UserHandle userHandle,
            PackageManager pm) throws XmlPullParserException, IOException {
    	...
    }
```

### Case 10

- From Entity : com.android.keyguard.EmergencyButton
- Relation : Define
- To Entity : com.android.keyguard.EmergencyButton.updateEmergencyCallButton

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 10)

```java
    public void updateEmergencyCallButton() { // Case 10
        boolean visible = false;
        ...
    }
```

#### Code fragment in OmniROM-android12 (Case 10)

```java
    void updateEmergencyCallButton(boolean isInCall, boolean isVoiceCapable, boolean simLocked) {  // Case 10
        boolean visible = false;
        ...
    }
```

### Case 11

- From Entity : android.telecom.ConnectionService
- Relation : Define
- To Entity : android.telecom.ConnectionService.answerVideo
- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 11)

```java
    protected void answerVideo(String callId, int videoState) { // Case 11
        Log.i(this, "answerVideo %s", callId);
    	...
    }
```

#### Code fragment in OmniROM-android12 (Case 11)

```java
    private void answerVideo(String callId, int videoState) { // Case 11
        Log.i(this, "answerVideo %s", callId);
        ...
    }
```

### Case 12

- From Entity : android.telecom.ConnectionService
- Relation : Define
- To Entity : android.telecom.ConnectionService.answer
- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 12)

```java
    protected void answer(String callId) { // Case 12
        Log.i(this, "answer %s", callId);
        ...
    }
```

#### Code fragment in OmniROM-android12 (Case 12)

```java
    private void answer(String callId) { // Case 12
        Log.i(this, "answer %s", callId);
        ...
    }
```

### Case 13

- From Entity : android.nfc.cardemulation.AidGroup
- Relation : Define
- To Entity : android.nfc.cardemulation.AidGroup.aids

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 13)

```java
public class AidGroup implements Parcelable {
    ...
    protected List<String> aids;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 13)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 14)

```java
public class AidGroup implements Parcelable {
    ...
    protected String category;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 14)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 15)

```java
public class AidGroup implements Parcelable {
    ...
    protected String description;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 15)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 16)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    protected ResolveInfo mService;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 16)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 17)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    protected String mDescription;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 17)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 18)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    protected boolean mOnHost;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 18)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 19)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    protected  HashMap<String, AidGroup> mStaticAidGroups;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 19)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 20)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    protected  HashMap<String, AidGroup> mDynamicAidGroups;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 20)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 21)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    protected boolean mRequiresDeviceUnlock;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 21)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 22)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    protected int mBannerResourceId;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 22)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 23)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    protected int mUid;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 23)

```java
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

- **modified line : 1**

#### Code fragment in OmniROM-android11 (Case 24)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    protected String mSettingsActivityName;
    ...
}
```

#### Code fragment in OmniROM-android12 (Case 24)

```java
public class ApduServiceInfo implements Parcelable {
    ...
    final String mSettingsActivityName;
    ...
}
```



## Table 1 Statistics on the number of lines of file code and complexity of files

**Q:For example, when analyzing the impact of design smell occurrence on change- and fault-proneness, it is unclear how the authors accounted for confounding factors such as object-oriented smells contained in the files, which are already known to be related to change- and fault-proneness. The authors also did not account for the confounding effects of size and complexity.**



**Concept Description：**

| Name            | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| project         | Andriod project name                                         |
| version         | Detailed version of project                                  |
| file_num        | the number of java files in the project                      |
| aff_num         | The number of java files with design smells                  |
| aff_avg_loc     | The average number of line of code in java files with design smells |
| aff_avg_cc      | The average $CC$ in java files with design smells            |
| CC              | The sum of Cyclomatic Complexity of methods in code file     |
| not_aff_num     | The number of java files **without** design smells           |
| not_aff_avg_loc | The average number of line of code in java files **without** design smells |
| not_aff_avg_cc  | The average $CC$ in java files **without** design smells     |



**Detailed Data:**

This table specify,  in 17 versions of 4 projects,  the statistic of LOC and Cyclomatic Complexity divided into two type by the design smell.

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



## Table 2 The correlation between the occurrence of design code smells in files and the file size as well as code complexity

**Q: same with Q in TABLE 1**

Based on the data from Table 1, analyze the correlation between the occurrence of design code smells in files and the file size as well as code complexity. The strength of this correlation is measured using p-values and effect size.

**Concept Description:**

| Name        | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| measure     | The name of metric                                           |
| p-value     | The possibility of that metric of aff is larger than that of non_aff |
| effect size | The standardized value of the mean difference between two sets of metrics, known as Cohen's d |

**Detailed Data:**

This table shows the the strength of this correlation measured by p-values and effect size.

| measure | P-value             | effect_size |
| ------- | ------------------- | ----------- |
| LOC     | 7.63E-06 < 0.000001 | 6.09        |
| CC      | 7.63E-06 < 0.000001 | 5.42        |

## Table 3 The precision and recall of design smells in relation to merge conflicts at the file level

This table specify the precision and recall of design smells in relation to merge conflicts at the file level.

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

This table specify the recall of design smells in relation to merge conflicts at the block level.

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

## Table 5 Average conflict count statistics for files with and without design smell involvement

The second column of this table represents the average number of conflict blocks in files with design smell involvement, while the third column represents the number of conflict blocks in files without design smell involvement.

| Project | *Conf_cap* | *Conf* |
| :-----: | :--------: | :----: |
|   A-T   |     2      |   4    |
|   A-S   |     4      |   4    |
|   A-R   |     5      |   3    |
|   A-Q   |     4      |   3    |
|  C-13   |     2      |   3    |
|  C-12   |     1      |   3    |
|  C-11   |     1      |   0    |
| L-20.0  |     4      |   0    |
| L-19.1  |     3      |   0    |
| L-18.1  |     5      |   2    |
| L-17.1  |     3      |   2    |
| L-16.0  |     2      |   1    |
| O-13.0  |     4      |   0    |
| O-12.0  |     2      |   1    |
|  O-11   |     7      |   3    |
|  O-10   |     2      |   2    |
|   O-9   |     2      |   1    |
|   I-E   |     5      |   2    |
|   I-D   |     5      |   2    |
|   I-C   |     5      |   2    |
|   I-B   |     5      |   2    |
|   I-A   |     4      |   3    |
| Average |     4      |   2    |

## Table 6 Validation results of duplicate conflict blocks across commits

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

## Table 7 Validation results of duplicate conflict blocks across versions

|  Project  | **Block** | **Text-50%** | **Manual** | Recall | Precision |
| :-------: | :-------: | :----------: | :--------: | :----: | :-------: |
|   AOSPA   |    819    |      35      |     37     | 94.59% |   100%    |
|  CalyxOS  |    143    |      0       |     0      |   0    |     0     |
| LineageOS |    321    |      9       |     9      |  100%  |   100%    |
|  OmniROM  |    623    |      4       |     4      |  100%  |   100%    |
|  Average  |    477    |      12      |     13     | 74.65% |  75.00%   |

## Table 8 Validation results of duplicate conflict blocks across projects

| **Project**  | **Block** | **Text-50%** | **Manual** | Recall | Precision |
| :----------: | :-------: | :----------: | :--------: | :----: | :-------: |
| Diff-project |   1906    |     672      |    648     |  100%  |  96.43%   |

