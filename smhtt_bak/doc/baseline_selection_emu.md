# Baseline Selection: e-mu


## electron

Kinematics:

```c++
ele.pt() > 13 && fabs(ele.eta()) < 2.5
```

Vertex:

```c++
fabs(electron.gsfTrack()->dxy(vtx.position())) < 0.045 &&
fabs(electron.gsfTrack()->dz(vtx.position()))  < 0.2
```

ID: [recommendations for 2017 data](https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentificationRun2#Recommended_MVA_Recipe_V2_for_re)

```python
MVA ID 90% efficiency WP 'egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp90'
```

In addition to the MVA ID, also require that the electron has no matched conversions and that the number of missing hits is <=1:

```c++
elec.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS))) <=1 &&
elec.passConversionVeto()
```

## muon

Kinematics:

```python
muon.pt() > 13 and
abs(muon.eta()) < 2.4
```

Vertex:

```c++
fabs(muon.muonBestTrack()->dxy(vtx.position())) < 0.045 &&
fabs(muon.muonBestTrack()->dz(vtx.position())) < 0.2
```

ID: [POG medium muon ID](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Short_Term_Medium_Muon_Definitio)

## e-mu pair

```
dR(e,mu) > 0.3
```

Require the OR of the trigger paths listed in [the trigger section](trigger_info.md#e-mu-triggers), matching the offline objects with the HLT objects with $`\Delta R<0.3`$.

An additional pT cut of pT>24 GeV should be applied to whichever object is firing the higher pT leg of the trigger.

## Final selection (post sync ntuple)

### electron

Isolation:

```python
iso < 0.15
```

### muon

Isolation:

```python
iso < 0.2
```

### Third lepton veto

See [definition](#third-lepton-veto), common to all channels. Reject event if any electron or muon (excluding signal muon and electron) passes this selection.
