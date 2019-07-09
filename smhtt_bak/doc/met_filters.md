# MET filters


Apply MET filters as recommended on the [MET filter TWiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2)

| Filter Name | MINIAOD flag | apply to | 
| ------------| -----------------------------|----------|
| primary vertex filter |	Flag_goodVertices | data & MC |
| beam halo filter |	Flag_globalSuperTightHalo2016Filter | 	data & MC
| HBHE noise filter |	Flag_HBHENoiseFilter |	data & MC
| HBHEiso noise filter |	Flag_HBHENoiseIsoFilter |  	data & MC
| ECAL TP filter | 	Flag_EcalDeadCellTriggerPrimitiveFilter |  	data & MC
| Bad PF Muon Filter |  	Flag_BadPFMuonFilter  | 	data & MC
| Bad Charged Hadron Filter |  	Flag_BadChargedCandidateFilter |  	data & MC
| ee badSC noise filter | 	Flag_eeBadScFilter |	data only
| ECAL bad calibration filter |  	Flag_ecalBadCalibFilter | 	data & MC


