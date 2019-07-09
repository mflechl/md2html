# Analysis ntuple format

This ntuple format is meant for both synchronization and analysis. It should therefore contain all the information needed for these two tasks.

We maintain two different variable naming schemes: 

* the new one, labelled `b`, documented below. 
* the old one, labelled `a`

the correspondance between the two schemes is described in [material/ntuple_format.txt](../material/ntuple_format.txt). 

the script [scripts/convert_ntuple.py](../scripts/convert_ntuple.py) can be used to rapidly and easily convert a sync ntuple from one naming scheme to the other. To be able to use it from anywere, go to the root of this package and do: 

```
source ./init.sh
```


For instructions on how to use it:  

```
convert_ntuple.py -h
```


## Event Information

| Variable      	| Description  | Comment |
| ------------- 	| ------------- | ---------- |
| run  			| run number | |
| lumi				| luminosity block number | |
| evt				| event number | |
| n\_up				| Number of partons. Useful to stitch the DY/W inclusive sample with the exclusive ones. ```Handle('source','LHEEventProduct').product().hepeup().NUP``` | we propose n_up instead of NUP by analogy with other counters |
| n\_pu				| Number of in-time pu interactions added to the event | n_pu instead of npu to identify counter|
| n\_pv				| number of offline primary vertices | n_pv instead of npv to identify counter |
| rho				| Use fixedGridRhoFastjetAll  | |
| is\_data			| True if data | | needed for analysis |

## Generator information

### Top pT reweighting

The following variables can be useful:

* in debugging top pT reweighting (can check that the base variables are at least the same)
* in applying a different pT reweighting after the fact for the analysis

Set them to 1 if not ttbar.

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| top1\_gen\_pt		| pt of leading top at gen level | |
| top2\_gen\_pt		| pt of subleading top | |

### Z pT reweighting

The following variables can be useful:

* in debugging Z pT reweighting (can check that the base variables are at least the same)
* in applying a different pT reweighting after the fact for the analysis

Set them to 1 for datasets other than DY M>50 GeV.

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| gen\_boson\_pt		| *(\*)* | |
| gen\_boson\_mass	| *(\*)* | |

*(\*) The gen boson is reconstructed in the following way:*

* access LHEEventProduct
* select all stable leptons (e, mu, tau, neutrinos)
* if exactly two leptons, sum their p4 and compute pt and mass


## Good event flags

Store each good event flag with the same name as in the MINIAOD:

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| Flag\_goodVertices | | |
| Flag\_globalTightHalo2016Filter | | |
| Flag\_HBHENoiseFilter | | |
| Flag\_HBHENoiseIsoFilter | | |
| Flag\_EcalDeadCellTriggerPrimitiveFilter | | |
| Flag\_BadPFMuonFilter | | |
| Flag\_BadChargedCandidateFilter | | |
| Flag\_eeBadScFilter | | |
| Flag\_ecalBadCalibFilter | | | |


## Extra lepton vetoes

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| veto\_dilepton | dilepton veto, if 1, kill event | dilepton\_veto replaced by veto\_dilepton to group all vetoes together |
| veto\_extra\_elec | third lepton veto, additional electron found. if 1, kill event | same |
| veto\_extra\_muon | third lepton veto, additional muon found. if 1, kill event | same |


## Trigger flags

**CHECK THAT THIS CORRESPONDS TO THE TRIGGERS USED IN THE ANALYSIS. FOR EXAMPLE, WHAT IF SEVERAL TAUTAU TRIGGERS ARE USED?**

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| trg\_singleelectron  | | |	 
| trg\_singlemuon 	  | | |
| trg\_singletau 	  | | |
| trg\_muonelectron 	  | | |
| trg\_mutaucross 	  | | |
| trg\_doubletau  | | | |

## Leptons

### Leg numbering convention

| Channel	| leg 1      |  leg 2     |
|---------|----------|---------|
| mu-tau  | mu		 | tau     |
| e-tau  	| e  		 | tau     |
| tau-tau  	| leading tau  		 | sub-leading tau     |
| e-mu  	| mu		 | e		 |
| mu-mu	| leading mu? | sub-leading mu?|
| e-e 		| leading e?  | sub-leading e? |

### Generic lepton information

For all types of leptons e, mu, or tau.

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| l1\_pt | | |
| l1\_eta | | |
| l1\_phi | | |
| l1\_m | | |
| l1\_q | | |
| l1\_weight\_idiso | | writing weight first to group the weight variables |
| l1\_weight\_trig | | writing weight first to group the weight variables |
| l1\_d0 | | |
| l1\_dz | | dz instead of dZ to comply to naming scheme (no need to think where to put capital letters)|
| l1\_gen_match |  |  |

### Electron specific

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| l1\_id\_e\_mva\_nt\_loose | Score of the non-triggering electron ID MVA | |
| l1\_weight\_tracking | | adding tracking weight (**is it needed this year?**). writing weight first to group the weight variables |
| l1\_iso | | |

### Muon specific

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| l1\_weight\_tracking | | adding tracking weight (**is it needed this year?**). writing weight first to group the weight variables |
| l1\_iso | | |

### Tau specific

We propose a simplified way to store the identification working points:

* less variables
* easier to apply at analysis level

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| l1\_weight\_fakerate | | needed for mssm qcd estimation |
| l1\_decayMode | | using capital letters to comply to the naming scheme of the tau ID group |
| l1\_againstElectronMVA6 | number of WP passed by the tau e.g. 1 if only loosest WP passed, 2 if two loosest WP passed, etc... | same |
| l1\_againstMuon3 | number of WP passed by the tau e.g. 1 if only loosest WP passed, 2 if two loosest WP passed, etc... | same |
| l1\_byIsolationMVArun2v1DBoldDMwLT | number of WP passed by the tau e.g. 1 if only loosest WP passed, 2 if two loosest WP passed, etc... | same |
| l1\_byIsolationMVArun2v1DBoldDMwLTraw | BDT score |  |
| l1\_chargedIsoPtSum | input to MVA | |
| l1\_neutralIsoPtSum | input to MVA | |
| l1\_puCorrPtSum | input to MVA | |
| l1\_footPrintCorrection | input to MVA | |
| l1\_photonPtSumOutsideSignalCone | input to MVA | |

## Jets

Counters:

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| n\_jets\_pt20 | See [inclusive jet selection](jet_selection.md#inclusive_jets)| |
| n\_jets\_pt30 | See [inclusive jet selection](jet_selection.md#inclusive_jets), but with pT>30 instead of pT>20 | for re-creating Run I categorization |
| n\_bjets | See [b jet selection](jet_selection.md#b_jets) | | changed nbtag to n\_bjets |

For inclusive jets, keep the two highest pt jets resulting from the [inclusive jet selection](jet_selection.md#inclusive_jets) (pT>20)

For b jets, keep the two highest pt b jets resulting from the [b jet selection](jet_selection.md#b_jets)

* `j*` denotes a variable of an inclusive jet
* `b*` denotes a variable of a b jet
* `*1` denotes a variable of the leading jet
* `*2` denotes a variable of the sub-leading jet

Example, for the leading inclusive jet:

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| j1\_pt | | |
| j1\_eta | | |
| j1\_phi | | |
| j1\_bcsv | | |
| j1\_pumva | | we propose to use jbmva instead of jmva for clarity to avoid possible conflicts with other jet mvas in the future|
| j1\_puid | 0: does not pass, 1:loose, 2:medium, 3:tight | |
| j1\_flavour\_parton | | useful to debug btag scale factors |
| j1\_flavour\_hadron | | useful to debug btag scale factors |
| j1\_rawf | factor needed to undo JEC | | |

## VBF

We propose a different naming scheme to clearly identify and group the vbf variables, see the Comment column.

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| mjj 		| ```(jet_1->vector()+jet_2->vector() ).M()```  | vbf_m?    |
| dijetpt | | vbf_pt ? |
| dijetphi| | vbf_phi ? |
| ptvis | ? **TODO: PROVIDE A DEFINITION** | vbf_ptvis ? |  
| jdeta	| delta eta between leading and subleading jets | vbf_deta? |
| jdphi | delta phi between leading and subleading jets | vbf_dphi? |  
| njetingap | Number of jets passing PF Jet ID and pt > 30, in eta gap | vbf_njetsingap? |  

**TODO: FOR NJETINGAP, SHOULDN'T WE SIMPLY REFER TO THE JET SELECTION SECTION? FOR EXAMPLE, THE OVERLAP REMOVAL IS NOT DISCUSSED HERE**

## MET, mT, pZeta

For each analysis, use the met agreed upon (e.g. MVA MET for SM and PF MET for MSSM).
Other flavours of MET can be added on the same model.

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| met | | |
| met\_phi | | |
| l1\_mt | $`\sqrt{2 p_{T,1} {\rm MET} (1-{\rm cos}(\Delta \phi)) }`$ |  |
| l2\_mt | $`\sqrt{2 p_{T,2} {\rm MET} (1-{\rm cos}(\Delta \phi)) }`$ |  |
| pzeta\_miss | | changed for clarity from pzetamiss |
| pzeta\_vis | | changed for clarity from pzetavis |
| metcov_00 | | |
| metcov_01 | | |
| metcov_10 | | |
| metcov_11 | | |


## Di-tau system

We propose a different naming scheme to group the di-lepton variables together.

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| m\_vis | | dil_m_vis? |
| m\_sv | | for SM only. dil\_m\_sv ? |
| mt\_sv | | for SM only. dil\_mt\_sv ? |
| mt\_tot | *(\*)* | dil\_mt\_tot ?|
| pt\_tt | $`(l_1 + l_2 + MET)_T`$, use PF met | dil\_pt ? |

*(\*)*

```math
m_{T,tot} = \sqrt{ 2 p_{T,1} {\rm MET} (1-{\rm cos}(\Delta \phi_1)) +  
2 p_{T,2} {\rm MET} (1-{\rm cos}(\Delta \phi_2)) +
2 p_{T,1} p_{T,2} (1-{\rm cos}(\Delta \phi_{12})) }
```

where $`\Delta \phi_1`$, $`\Delta \phi_2`$, and $`\Delta \phi_{12}`$ are the differences in azimuth between the first leg and the MET, the second leg and the MET, and the two legs, respectively.

## Other weights

| Variable      		| Description  | Comment |
| ------------- 		| ------------- | ---------- |
| weight				| global event weight | first, synchronize individual weights |
| weight\_pu			| pileup weight | changing from puweight, so that all weights appear together |
| weight\_dy			| Drell-Yan pT weight, set to 1 if not DY |  |
| weight\_top  		| ttbar pT weight, set to 1 if not top | |
| weight\_njet		| stitching weight for DYJets and WJets, set to 1 otherwise |  |
