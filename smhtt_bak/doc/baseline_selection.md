# Baseline selection

Compared to the Run I analysis we have decided to follow a modified workflow for the event selection and synchronisation, cf. [these slides](https://indico.cern.ch/event/376387/session/17/contribution/18/material/slides/0.pdf). The workflow is summarized as follows, and all details are given in the sections below.

* Create collection of selected e/mu/tau using only basic ID and kinematic cuts as defined in the following section.
* Create a list of all the possible pairs, then filter this list for those pairs which do not satisfy the $`\Delta R`$ requirements
* Take the most isolated pair (with no os/ss preference) by sorting the pairs as described in the next subsection
* Make sync ntuples
* The remaining analysis selection, e.g: isolation cuts, trigger(s), filter(s), anti-electron and anti-muon discriminators for the taus, extra lepton vetoes are then applied on top of the sync ntuple selection as event-level properties.
* OS requirement can then be defined for signal events, SS and anti-iso used for control regions (and both sets of events are now totally exclusive).

## Pair selection algorithm

Following the ID, pt/eta cuts, and dR condition, there will be more than one possible candidate pair. We resolve this by selecting the pair with the two most isolated leptons, under the assumption that this gives the highest efficiency for selecting the correct pair in signal events.

The following is mandatory logic for comparing two pairs in a sorting algorithm that aims to resolve ambiguous cases (e.g. multiple candidates with the same isolation value) if trying to perform synchronization:

   * First prefer the pair with the most isolated candidate 1 (muon mu-tau and e-mu, electron for e-tau and either tau for tau-tau).
   * If the isolation of candidate 1 is the same in both pairs, prefer the pair with the highest candidate 1 pt (for cases of genuinely the same isolation value but different possible candidate 1).
   * If the pt of candidate 1 in both pairs is the same (likely because it's the same object) then prefer the pair with the most isolated candidate 2 (tau for e-tau, mu-tau, tau-tau, electron for e-mu).
   * If the isolation of candidate 2 is the same, prefer the pair with highest candidate 2 pt (for cases of genuinely the same isolation value but different possible candidate 2).

For taus, sort by raw MVA isolation `byIsolationMVArun2017v2DBoldDMwLTraw2017`.

To use this logic in the tau-tau channel each possible pairing should appear **twice** in the collection of pairs, to account for each of the taus appearing as candidate 1 and the other as candidate 2.

**For details about object reconstruction, identification, and isolation, please see [the offline reconstruction section](offline_reco.md)**

## Channels

* [Baseline mu-tau](baseline_selection_mutau.md)
* [Baseline e-tau](baseline_selection_etau.md)
* [Baseline tau-tau](baseline_selection_tautau.md)
* [Baseline e-mu](baseline_selection_emu.md)
* [Baseline mu-mu](baseline_selection_mumu.md)
* [Baseline e-e](baseline_selection_ee.md)

### Third lepton veto

The definition of the third lepton veto is common to all channels.

Electron

```python
ele.pt()         > 10                                                                                 and
fabs(ele.eta())  < 2.5                                                                                and
fabs(dxy)        < 0.045                                                                              and
fabs(dz)         < 0.2                                                                                and
MVA ID 90% efficiency WP 'egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp90'                            and
elec.passConversionVeto()                                                                             and
elec.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS))) <=1            and
iso              < 0.3
```

Muon

```python
muon.pt()        > 10                            and
fabs(muon.eta)   < 2.4                           and
fabs(dxy)        < 0.045                         and
fabs(dz)         < 0.2                           and
'Medium' ID                                      and
iso              < 0.3
```

The `dz, dxy, iso` variables are defined as for the nominal object selection above.
