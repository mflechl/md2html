# Baseline Selection: mu-tau


## muon

Kinematics:

```python
muon.pt() > 21 and
abs(muon.eta()) < 2.1
```

Vertex:

```c++
fabs(muon.muonBestTrack()->dxy(vtx.position())) < 0.045 &&
fabs(muon.muonBestTrack()->dz(vtx.position()))  < 0.2
```

ID: [Medium muon ID](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Short_Term_Medium_Muon_Definitio)

## tau

Kinematics:

```python
tau.pt() > 20 and
fabs(tau.eta()) < 2.3 and
```

ID: [TauIDRecommendation13TeV](https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV)

```python
tau.tauID('decayModeFinding') > 0.5                  and
'byVVLooseIsolationMVArun2017v2DBoldDMwLT2017'       and
tau.charge() in [1,-1]
```

Vertex:

```c++
pat::PackedCandidate const* packedLeadTauCand = dynamic_cast<pat::PackedCandidate const*>(src.leadChargedHadrCand().get())
fabs(packedLeadTauCand->dz()) < 0.2  # The PackedCandidate::dz() method is wrt. the first PV by default
```

## mu-tau pair

```python
dR(mu, tau) > 0.5
```

Require the OR of the trigger paths listed in [the trigger section](trigger_info.md#mu-tau-triggers), matching the offline objects with the HLT objects with $`\Delta R<0.5`$.

## Final selection (post sync ntuple)

### muon

Isolation

```python
iso < 0.15
```

### tau

[TauIDRecommendation13TeV](https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV)

* ID

```python
tau.tauID('againstElectronVLooseMVA6')      > 0.5  and
tau.tauID('againstMuonTight3')              > 0.5
```

* Isolation: run2 MVA, oldDMs

```python
tau.tauID('byTightIsolationMVArun2017v2DBoldDMwLT2017') > 0.5
```

### Di-muon veto

Muons considered for the di-muon veto should verify the following requirements :

```python
muon.pt() > 15                 and
fabs(muon.eta()) < 2.4         and
muon.isLooseMuon()             and
dz  < 0.2                      and
dxy < 0.045                    and
iso < 0.3
```
This selection is looser in pt, eta, ID and iso than the one applied in the [baseline selection](#muon). Therefore, the muon selected for the construction of the di-tau pair is always considered by the di-muon veto.

The di-muon veto rejects events in which any pair of such muons verifies the following requirements :

```python
muon1.q() * muon2.q() < 0 and
dR(muon1, muon2) > 0.15
```

### Third lepton veto

See [definition](baseline_selection.md#third-lepton-veto), common to all channels. Reject event if any electron or muon (excluding signal muon) passes this selection.
