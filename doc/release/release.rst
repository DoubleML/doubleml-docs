:parenttoc: True

Release Notes
=============

.. tab-set::

  .. tab-item:: Python

    .. dropdown:: DoubleML 0.10.0
      :class-title: sd-bg-primary sd-font-weight-bold
      :open:

      - **Release highlight:** Multi-Period Difference-in-Differences for Panel Data

        - Implementation via ``DoubleMLDIDMulti`` class
          `Py #292 <https://github.com/DoubleML/doubleml-for-py/pull/292>`_
          `Py #315 <https://github.com/DoubleML/doubleml-for-py/pull/315>`_
        - New ``doubleml.data`` submodule including ``DoubleMLData`` and ``DoubleMLPanelData`` classes
          `Py #292 <https://github.com/DoubleML/doubleml-for-py/pull/292>`_
        - Extended User Guide and Example Gallery
          `Docs #224 <https://github.com/DoubleML/doubleml-docs/pull/224>`_
          `Docs #233 <https://github.com/DoubleML/doubleml-docs/pull/233>`_
          `Docs #237 <https://github.com/DoubleML/doubleml-docs/pull/237>`_

      - Added Confidence sets which are robust to weak IVs: ``robust_confset()`` method for ``DoubleMLIIVM``
        (added by `Ezequiel Smucler <https://github.com/esmucler>`_ and `David Masip <https://github.com/david26694>`_)
        `Py #318 <https://github.com/DoubleML/doubleml-for-py/pull/318>`_
        `Docs #234 <https://github.com/DoubleML/doubleml-docs/pull/234>`_

      - Update sensitivity operations to improve sensitivity bounds
        `Py #295 <https://github.com/DoubleML/doubleml-for-py/pull/295>`_

      - Improve ``DoubleMLAPO`` nuisance estimation and update weighted score elements.
        Added example to compare ``DoubleMLIRM`` and ``DoubleMLAPO``.
        `Py #295 <https://github.com/DoubleML/doubleml-for-py/pull/295>`_
        `Py #297 <https://github.com/DoubleML/doubleml-for-py/pull/297>`_
        `Docs #220 <https://github.com/DoubleML/doubleml-docs/pull/220>`_

      - Updated variance aggregation over repetitions via confidence intervals
        `Py #324 <https://github.com/DoubleML/doubleml-for-py/pull/324>`_
        `Docs #236 <https://github.com/DoubleML/doubleml-docs/pull/236>`_

      - Added a separate package citation using `CITATION.cff`
        `Py #321 <https://github.com/DoubleML/doubleml-for-py/pull/321>`_

      - Update package formatting, linting and add pre-commit hooks
        `Py #288 <https://github.com/DoubleML/doubleml-for-py/pull/288>`_
        `Py #289 <https://github.com/DoubleML/doubleml-for-py/pull/289>`_
        `Py #294 <https://github.com/DoubleML/doubleml-for-py/pull/294>`_
        `Py #316 <https://github.com/DoubleML/doubleml-for-py/pull/316>`_

      - Maintenance package
        `Py #287 <https://github.com/DoubleML/doubleml-for-py/pull/287>`_
        `Py #288 <https://github.com/DoubleML/doubleml-for-py/pull/288>`_
        `Py #291 <https://github.com/DoubleML/doubleml-for-py/pull/291>`_
        `Py #319 <https://github.com/DoubleML/doubleml-for-py/pull/319>`_

      - Maintenance documentation
        `Docs #211 <https://github.com/DoubleML/doubleml-docs/pull/211>`_
        `Docs #213 <https://github.com/DoubleML/doubleml-docs/pull/213>`_
        `Docs #214 <https://github.com/DoubleML/doubleml-docs/pull/214>`_
        `Docs #215 <https://github.com/DoubleML/doubleml-docs/pull/215>`_
        `Docs #216 <https://github.com/DoubleML/doubleml-docs/pull/216>`_
        `Docs #217 <https://github.com/DoubleML/doubleml-docs/pull/217>`_
        `Docs #218 <https://github.com/DoubleML/doubleml-docs/pull/218>`_
        `Docs #219 <https://github.com/DoubleML/doubleml-docs/pull/219>`_
        `Docs #221 <https://github.com/DoubleML/doubleml-docs/pull/221>`_
        `Docs #225 <https://github.com/DoubleML/doubleml-docs/pull/225>`_
        `Docs #227 <https://github.com/DoubleML/doubleml-docs/pull/227>`_
        `Docs #228 <https://github.com/DoubleML/doubleml-docs/pull/228>`_
        `Docs #229 <https://github.com/DoubleML/doubleml-docs/pull/229>`_
        `Docs #230 <https://github.com/DoubleML/doubleml-docs/pull/230>`_
        `Docs #232 <https://github.com/DoubleML/doubleml-docs/pull/232>`_
        `Docs #238 <https://github.com/DoubleML/doubleml-docs/pull/238>`_
        `Docs #239 <https://github.com/DoubleML/doubleml-docs/pull/239>`_

    .. dropdown:: DoubleML 0.9.3
      :class-title: sd-bg-primary sd-font-weight-bold

      - Fix / adapted unit tests which failed in the release of 0.9.2 to conda-forge
        `Docs #208 <https://github.com/DoubleML/doubleml-docs/pull/208>`_

    .. dropdown:: DoubleML 0.9.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - Make `rdrobust` optional for conda. Create `pyproject.toml` and remove `setup.py` for packaging
        `Py #285 <https://github.com/DoubleML/doubleml-for-py/pull/285>`_
        `Py #286 <https://github.com/DoubleML/doubleml-for-py/pull/286>`_

      - Maintenance package
        `Py #284 <https://github.com/DoubleML/doubleml-for-py/pull/284>`_

      - Maintenance documentation
        `Docs #205 <https://github.com/DoubleML/doubleml-docs/pull/205>`_
        `Docs #206 <https://github.com/DoubleML/doubleml-docs/pull/206>`_
        `Docs #207 <https://github.com/DoubleML/doubleml-docs/pull/207>`_
    
    .. dropdown:: DoubleML 0.9.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Regression Discontinuity Designs with Flexible Covariate Adjustment
        via ``RDFlex`` class (in cooperation with `Claudia Noack <https://github.com/claudianoack>`_
        and `Tomasz Olma <https://github.com/tomaszolma>`_; see `their paper <https://arxiv.org/abs/2107.07942>`_)
        `Py #276 <https://github.com/DoubleML/doubleml-for-py/pull/276>`_

      - Add ``cov_type=HC0`` and enable key-worded arguments to ``DoubleMLBLP``
        `Py #270 <https://github.com/DoubleML/doubleml-for-py/issues/270>`_
        `Py #271 <https://github.com/DoubleML/doubleml-for-py/pull/271>`_

      - Update User Guide and Example Gallery
        `Docs #204 <https://github.com/DoubleML/doubleml-docs/pull/204>`_

      - Add AutoML example for tuning DoubleML estimators
        `Docs #199 <https://github.com/DoubleML/doubleml-docs/pull/199>`_

      - Maintenance package
        `Py #268 <https://github.com/DoubleML/doubleml-for-py/pull/268>`_
        `Py #278 <https://github.com/DoubleML/doubleml-for-py/issues/278>`_
        `Py #279 <https://github.com/DoubleML/doubleml-for-py/pull/279>`_
        `Py #281 <https://github.com/DoubleML/doubleml-for-py/pull/281>`_
        `Py #282 <https://github.com/DoubleML/doubleml-for-py/pull/282>`_

      - Maintenance documentation
        `Docs #201 <https://github.com/DoubleML/doubleml-docs/pull/201>`_
        `Docs #203 <https://github.com/DoubleML/doubleml-docs/pull/203>`_

    .. dropdown:: DoubleML 0.9.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Average potential outcomes for multiple discrete treatments
        via ``DoubleMLAPO`` and ``DoubleMLAPOS`` classes (proposed by `Apoorva Lal <https://github.com/apoorvalal>`_)
        `Py #245 <https://github.com/DoubleML/doubleml-for-py/issues/245>`_
        `Py #250 <https://github.com/DoubleML/doubleml-for-py/pull/250>`_

      - Update User Guide and Example Gallery
        `Docs #188 <https://github.com/DoubleML/doubleml-docs/pull/188>`_
        `Docs #195 <https://github.com/DoubleML/doubleml-docs/pull/195>`_

      - Add sensitivity analysis to ``DoubleMLFramework``
        `Py #249 <https://github.com/DoubleML/doubleml-for-py/pull/249>`_

      - Maintenance package
        `Py #264 <https://github.com/DoubleML/doubleml-for-py/pull/264>`_
        `Py #265 <https://github.com/DoubleML/doubleml-for-py/pull/265>`_
        `Py #266 <https://github.com/DoubleML/doubleml-for-py/pull/266>`_

      - Maintenance documentation
        `Docs #182 <https://github.com/DoubleML/doubleml-docs/pull/182>`_
        `Docs #184 <https://github.com/DoubleML/doubleml-docs/pull/184>`_
        `Docs #186 <https://github.com/DoubleML/doubleml-docs/pull/186>`_
        `Docs #193 <https://github.com/DoubleML/doubleml-docs/pull/193>`_
        `Docs #194 <https://github.com/DoubleML/doubleml-docs/pull/194>`_
        `Docs #196 <https://github.com/DoubleML/doubleml-docs/pull/196>`_
        `Docs #197 <https://github.com/DoubleML/doubleml-docs/pull/197>`_

    .. dropdown:: DoubleML 0.8.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - **API Update**: Change nuisance evaluation for classifiers.
        The corresponding properties are renamed ``nuisance_loss`` instead of ``rmses``.
        `Py #254 <https://github.com/DoubleML/doubleml-for-py/pull/254>`_
        `Docs #184 <https://github.com/DoubleML/doubleml-docs/pull/184>`_

      - Add new example on sensitivity analysis
        `Docs #190 <https://github.com/DoubleML/doubleml-docs/pull/190>`_

      - Add a new example on DiD with DoubleML in R
        `Docs #178 <https://github.com/DoubleML/doubleml-docs/pull/178>`_

      - Enable ``set_sample_splitting`` for cluster data
        `Py #255 <https://github.com/DoubleML/doubleml-for-py/pull/255>`_

      - Update the ``make_confounded_irm_data`` data generating process
        `Py #263 <https://github.com/DoubleML/doubleml-for-py/pull/263>`_
      
      - Maintenance package
        `Py #264 <https://github.com/DoubleML/doubleml-for-py/pull/264>`_

      - Maintenance documentation
        `Docs #177 <https://github.com/DoubleML/doubleml-docs/pull/177>`_
        `Docs #180 <https://github.com/DoubleML/doubleml-docs/pull/180>`_
        `Docs #181 <https://github.com/DoubleML/doubleml-docs/pull/181>`_
        `Docs #187 <https://github.com/DoubleML/doubleml-docs/pull/187>`_
        `Docs #189 <https://github.com/DoubleML/doubleml-docs/pull/189>`_

    .. dropdown:: DoubleML 0.8.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Increment package requirements and update workflows for python 3.9 (add tests for python 3.12)
        `Py #247 <https://github.com/DoubleML/doubleml-for-py/pull/247>`_
        `Docs #175 <https://github.com/DoubleML/doubleml-docs/pull/175>`_

      - Additional example for ranking treatment effects (by `Apoorva Lal <https://github.com/apoorvalal>`_)
        `Docs #173 <https://github.com/DoubleML/doubleml-docs/pull/173>`_
        `Docs #174 <https://github.com/DoubleML/doubleml-docs/pull/174>`_

      - Maintenance documentation
        `Docs #172 <https://github.com/DoubleML/doubleml-docs/pull/172>`_

    .. dropdown:: DoubleML 0.8.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Sample-selections models as ``DoubleMLSMM`` class (by `Michaela Kecskésová <https://github.com/mychaelka>`_)
        `Py #231 <https://github.com/DoubleML/doubleml-for-py/pull/231>`_
        `Py #235 <https://github.com/DoubleML/doubleml-for-py/pull/235>`_
        `Docs #171 <https://github.com/DoubleML/doubleml-docs/pull/171>`_
      - **API change:** Remove options ``apply_crossfitting`` and ``dml_procedure`` from the ``DoubleML`` class
        `Py #227 <https://github.com/DoubleML/doubleml-for-py/pull/227>`_
        `Docs #166 <https://github.com/DoubleML/doubleml-docs/pull/166>`_
      - Restructure the package to improve readability and maintainability
        `Py #225 <https://github.com/DoubleML/doubleml-for-py/pull/225>`_
      - Add a ``DoubleMLFramework`` class to combine multiple DoubleML models (aggregation of estimates, boostrap and CI-procedures)
        `Py #226 <https://github.com/DoubleML/doubleml-for-py/pull/226>`_
        `Docs #169 <https://github.com/DoubleML/doubleml-docs/pull/169>`_
      - Enable the use of external predictions for short models in benchmarks (by `Lucien <https://github.com/lucien1011>`_)
        `Py #238 <https://github.com/DoubleML/doubleml-for-py/pull/238>`_
        `Py #239 <https://github.com/DoubleML/doubleml-for-py/pull/239>`_
      - Add the ``gain_statistics`` to ``utils`` to sensitivity analysis
        `Py #229 <https://github.com/DoubleML/doubleml-for-py/pull/229>`_

      - Maintenance documentation
        `Docs #162 <https://github.com/DoubleML/doubleml-docs/pull/162>`_
        `Docs #163 <https://github.com/DoubleML/doubleml-docs/pull/163>`_
        `Docs #164 <https://github.com/DoubleML/doubleml-docs/pull/164>`_
        `Docs #165 <https://github.com/DoubleML/doubleml-docs/pull/165>`_
        `Docs #167 <https://github.com/DoubleML/doubleml-docs/pull/167>`_
        `Docs #168 <https://github.com/DoubleML/doubleml-docs/pull/168>`_

      - Maintenance package
        `Py #225 <https://github.com/DoubleML/doubleml-for-py/pull/225>`_
        `Py #229 <https://github.com/DoubleML/doubleml-for-py/pull/229>`_
        `Py #246 <https://github.com/DoubleML/doubleml-for-py/pull/246>`_

    .. dropdown:: DoubleML 0.7.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Add weights to ``DoubleMLIRM`` class to extend sensitivity to GATEs etc.
        `Py #220 <https://github.com/DoubleML/doubleml-for-py/pull/220>`_
        `Py #229 <https://github.com/DoubleML/doubleml-for-py/pull/229>`_
        `Docs #155 <https://github.com/DoubleML/doubleml-docs/pull/155>`_
        `Docs #161 <https://github.com/DoubleML/doubleml-docs/pull/161>`_
      - Extend GATE and CATE estimation to the ``DoubleMLPLR`` class
        `Py #220 <https://github.com/DoubleML/doubleml-for-py/pull/220>`_
        `Docs #155 <https://github.com/DoubleML/doubleml-docs/pull/155>`_
      - Enable the use of external predictions for ``DoubleML`` classes
        `Py #221 <https://github.com/DoubleML/doubleml-for-py/pull/221>`_
        `Docs #159 <https://github.com/DoubleML/doubleml-docs/pull/159>`_

      - Implementing utility classes and functions (gain statistics and dummy learners)
        `Py #221 <https://github.com/DoubleML/doubleml-for-py/pull/221>`_
        `Py #222 <https://github.com/DoubleML/doubleml-for-py/pull/222>`_
        `Py #229 <https://github.com/DoubleML/doubleml-for-py/pull/229>`_
        `Docs #161 <https://github.com/DoubleML/doubleml-docs/pull/161>`_

      - Extend example Gallery
        `Docs #153 <https://github.com/DoubleML/doubleml-docs/pull/153>`_
        `Docs #158 <https://github.com/DoubleML/doubleml-docs/pull/158>`_
        `Docs #161 <https://github.com/DoubleML/doubleml-docs/pull/161>`_

      - Maintenance documentation
        `Docs #157 <https://github.com/DoubleML/doubleml-docs/pull/157>`_
        `Docs #160 <https://github.com/DoubleML/doubleml-docs/pull/160>`_

      - Maintenance package
        `Py #223 <https://github.com/DoubleML/doubleml-for-py/pull/223>`_
        `Py #224 <https://github.com/DoubleML/doubleml-for-py/pull/224>`_


    .. dropdown:: DoubleML 0.7.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Benchmarking for Sensitivity Analysis (omitted variable bias)
        `Py #211 <https://github.com/DoubleML/doubleml-for-py/pull/211>`_
      - Policy tree estimation for the ``DoubleMLIRM`` class
        `Py #212 <https://github.com/DoubleML/doubleml-for-py/pull/212>`_

      - Extending sensitivity and policy tree documentation in User Guide and Example Gallery
        `Docs #148 <https://github.com/DoubleML/doubleml-docs/pull/148>`_
        `Docs #150 <https://github.com/DoubleML/doubleml-docs/pull/150>`_

      - The package requirements are set to python 3.8 or higher
        `Py #211 <https://github.com/DoubleML/doubleml-for-py/pull/211>`_
      
      - Maintenance documentation
        `Docs #149 <https://github.com/DoubleML/doubleml-docs/pull/149>`_
      - Maintenance package
        `Py #213 <https://github.com/DoubleML/doubleml-for-py/pull/213>`_

    .. dropdown:: DoubleML 0.6.3
      :class-title: sd-bg-primary sd-font-weight-bold

      - Fix install requirements for 0.6.2
        `Py #208 <https://github.com/DoubleML/doubleml-for-py/pull/208>`_

    .. dropdown:: DoubleML 0.6.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Sensitivity Analysis (omitted variable bias) for
        `Py #201 <https://github.com/DoubleML/doubleml-for-py/pull/201>`_

        - ``DoubleMLPLR``
        - ``DoubleMLIRM``
        - ``DoubleMLDID``
        - ``DoubleMLDIDCS``
      
      - Updated documentation
        `Docs #144 <https://github.com/DoubleML/doubleml-docs/pull/144>`_
        `Docs #141 <https://github.com/DoubleML/doubleml-docs/pull/141>`_

      - Extend the guide with sensitivity and add further examples
        `Docs #142 <https://github.com/DoubleML/doubleml-docs/pull/142>`_

      - Maintenance package
        `Py #202 <https://github.com/DoubleML/doubleml-for-py/pull/202>`_
        `Py #206 <https://github.com/DoubleML/doubleml-for-py/pull/206>`_

      - Maintenance documentation
        `Docs #137 <https://github.com/DoubleML/doubleml-docs/pull/137>`_
        `Docs #138 <https://github.com/DoubleML/doubleml-docs/pull/138>`_
        `Docs #140 <https://github.com/DoubleML/doubleml-docs/pull/140>`_
        `Docs #143 <https://github.com/DoubleML/doubleml-docs/pull/143>`_
        `Docs #145 <https://github.com/DoubleML/doubleml-docs/pull/145>`_
        `Docs #146 <https://github.com/DoubleML/doubleml-docs/pull/146>`_

    .. dropdown:: DoubleML 0.6.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Difference-in-differences models for ATTE estimation
        `Py #200 <https://github.com/DoubleML/doubleml-for-py/pull/200>`_
        `Py #194 <https://github.com/DoubleML/doubleml-for-py/issues/194>`_

        - Panel data ``DoubleMLDID``
        - Repeated cross sections ``DoubleMLDIDCS``
      
      - Add a potential time variable to ``DoubleMLData`` (until now only used in ``DoubleMLDIDCS``)
        `Py #200 <https://github.com/DoubleML/doubleml-for-py/pull/200>`_

      - Extend the guide in the documentation and add further examples
        `Docs #132 <https://github.com/DoubleML/doubleml-docs/pull/132>`_
        `Docs #133 <https://github.com/DoubleML/doubleml-docs/pull/133>`_
        `Docs #135 <https://github.com/DoubleML/doubleml-docs/pull/135>`_

      - Maintenance
        `Py #199 <https://github.com/DoubleML/doubleml-for-py/pull/199>`_
        `Docs #134 <https://github.com/DoubleML/doubleml-docs/pull/134>`_
        `Docs #136 <https://github.com/DoubleML/doubleml-docs/pull/136>`_  

    .. dropdown:: DoubleML 0.6.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Heterogeneous treatment effects (GATE, CATE, Quantile effects, ...)
      - Add out-of-sample RMSE and targets for nuisance elements and implement nuisance estimation 
        evaluation via ``evaluate_learners()``.
        `Py #182 <https://github.com/DoubleML/doubleml-for-py/pull/182>`_
        `Py #188 <https://github.com/DoubleML/doubleml-for-py/pull/188>`_
      - Implement ``gate()`` and ``cate()`` methods for ``DoubleMLIRM`` class. Both are 
        based on the new ``DoubleMLBLP`` class.
        `Py #169 <https://github.com/DoubleML/doubleml-for-py/pull/169>`_
      - Implement different type of quantile models
        `Py #179 <https://github.com/DoubleML/doubleml-for-py/pull/179>`_
        
        - Potential quantiles (PQ) in class ``DoubleMLPQ``
        - Local potential quantiles (LPQ) in class ``DoubleMLLPQ``
        - Conditional value at risk (CVaR) in class ``DoubleMLCVAR``
        - Quantile treatment effects (QTE) in class ``DoubleMLQTE``

      - Extend clustering to nonlinear scores
        `Py #190 <https://github.com/DoubleML/doubleml-for-py/pull/190>`_
      - Add ``ipw_normalization`` option to ``DoubleMLIRM`` and ``DoubleMLIIVM``
        `Py #186 <https://github.com/DoubleML/doubleml-for-py/pull/186>`_
      - Implement an abstract base class for data backends 
        `Py #173 <https://github.com/DoubleML/doubleml-for-py/pull/173>`_
      - Extend the guide in the documentation and add further examples
        `Docs #116 <https://github.com/DoubleML/doubleml-docs/pull/116>`_
        `Docs #125 <https://github.com/DoubleML/doubleml-docs/pull/125>`_
        `Docs #126 <https://github.com/DoubleML/doubleml-docs/pull/126>`_
      - Code refactorings, bug fixes, docu updates, unit test extensions and continuous integration
        `Py #183 <https://github.com/DoubleML/doubleml-for-py/pull/183>`_
        `Py #192 <https://github.com/DoubleML/doubleml-for-py/pull/192>`_
        `Py #195 <https://github.com/DoubleML/doubleml-for-py/pull/195>`_
        `Py #196 <https://github.com/DoubleML/doubleml-for-py/pull/196>`_
      - Change License to BSD 3-Clause
        `Py #198 <https://github.com/DoubleML/doubleml-for-py/pull/198>`_
      - Maintenance
        `Py #174 <https://github.com/DoubleML/doubleml-for-py/pull/174>`_
        `Py #178 <https://github.com/DoubleML/doubleml-for-py/pull/178>`_
        `Py #181 <https://github.com/DoubleML/doubleml-for-py/pull/181>`_

    .. dropdown:: DoubleML 0.5.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - Fix / adapted unit tests which failed in the release of 0.5.1 to conda-forge
        `Py #172 <https://github.com/DoubleML/doubleml-for-py/pull/172>`_

    .. dropdown:: DoubleML 0.5.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Store estimated models for nuisance parameters
        `Py #159 <https://github.com/DoubleML/doubleml-for-py/pull/159>`_
      - Bug fix: Overwrite for tune method (introduced for depreciation warning) did not return the tune result
        `Py #160 <https://github.com/DoubleML/doubleml-for-py/pull/160>`_
        `Py #162 <https://github.com/DoubleML/doubleml-for-py/issues/162>`_
      - Maintenance
        `Py #166 <https://github.com/DoubleML/doubleml-for-py/pull/166>`_
        `Py #167 <https://github.com/DoubleML/doubleml-for-py/pull/167>`_
        `Py #168 <https://github.com/DoubleML/doubleml-for-py/pull/168>`_
        `Py #170 <https://github.com/DoubleML/doubleml-for-py/pull/170>`_

    .. dropdown:: DoubleML 0.5.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Implement a new score function ``score = 'IV-type'`` for the PLIV model (for details see
        `Py #151 <https://github.com/DoubleML/doubleml-for-py/pull/151>`_) |br|
        --> **API change** from ``DoubleMLPLIV(obj_dml_data, ml_g, ml_m, ml_r [, ...])``
        to ``DoubleMLPLIV(obj_dml_data, ml_g, ml_m, ml_r, ml_g [, ...])``
      - Adapt the nuisance estimation for the ``'IV-type'`` score for the PLR model (for details see
        `Py #151 <https://github.com/DoubleML/doubleml-for-py/pull/151>`_) |br|
        --> **API change** from ``DoubleMLPLR(obj_dml_data, ml_g, ml_m [, ...])``
        to ``DoubleMLPLR(obj_dml_data, ml_l, ml_m, ml_g [, ...])``
      - Allow the usage of classifiers for binary outcome variables in the model classes IRM and IIVM
        `Py #134 <https://github.com/DoubleML/doubleml-for-py/pull/134>`_
      - **Published in JMLR: DoubleML - An Object-Oriented Implementation of Double Machine Learning in Python** (citation
        info updated in `Py #138 <https://github.com/DoubleML/doubleml-for-py/pull/138>`_)
      - Maintenance
        `Py #143 <https://github.com/DoubleML/doubleml-for-py/pull/143>`_
        `Py #148 <https://github.com/DoubleML/doubleml-for-py/pull/148>`_
        `Py #149 <https://github.com/DoubleML/doubleml-for-py/pull/149>`_
        `Py #152 <https://github.com/DoubleML/doubleml-for-py/issues/152>`_
        `Py #153 <https://github.com/DoubleML/doubleml-for-py/pull/153>`_

    .. dropdown:: DoubleML 0.4.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - We added `Python Contribution Guidelines <https://github.com/DoubleML/doubleml-for-py/blob/main/CONTRIBUTING.md>`_,
        issue templates, a pull request template and a
        `Python discussion forum <https://github.com/DoubleML/doubleml-for-py/discussions>`_ to the Python package repository
        `Py #132 <https://github.com/DoubleML/doubleml-for-py/pull/132>`_
      - Code refactorings, docu updates, unit test extensions and continuous integration
        `Py #126 <https://github.com/DoubleML/doubleml-for-py/pull/126>`_
        `Py #127 <https://github.com/DoubleML/doubleml-for-py/pull/127>`_
        `Py #128 <https://github.com/DoubleML/doubleml-for-py/pull/128>`_
        `Py #130 <https://github.com/DoubleML/doubleml-for-py/pull/130>`_
        `Py #131 <https://github.com/DoubleML/doubleml-for-py/pull/131>`_

    .. dropdown:: DoubleML 0.4.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Clustered standard errors for double machine learning models
        `Py #116 <https://github.com/DoubleML/doubleml-for-py/pull/116>`_
      - Improve exception handling for missings and infinite values in the confounders, predictions, etc.
        (fixes `Py #120 <https://github.com/DoubleML/doubleml-for-py/issues/120>`_ by allowing null confounder values)
        `Py #122 <https://github.com/DoubleML/doubleml-for-py/pull/122>`_
      - Clean up dev requirements and use dev requirements on github actions
        `Py #121 <https://github.com/DoubleML/doubleml-for-py/pull/121>`_
      - Other updates
        `Py #123 <https://github.com/DoubleML/doubleml-for-py/pull/123>`_

    .. dropdown:: DoubleML 0.3.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Always use the same bootstrap algorithm independent of ``dml1`` vs ``dml2`` and consistent with docu and paper
        `Py #101 <https://github.com/DoubleML/doubleml-for-py/issues/101>`_ &
        `Py #102 <https://github.com/DoubleML/doubleml-for-py/pull/102>`_
      - Added an exception handling to assure that an IV variable is specified when using a PLIV or IIVM model
        `Py #107 <https://github.com/DoubleML/doubleml-for-py/pull/107>`_
      - Improve exception handling for externally provided sample splitting
        `Py #110 <https://github.com/DoubleML/doubleml-for-py/pull/110>`_
      - Minor update of the str representation of ``DoubleMLData`` objects
        `Py #112 <https://github.com/DoubleML/doubleml-for-py/pull/112>`_
      - Code refactorings and unit test extensions
        `Py #103 <https://github.com/DoubleML/doubleml-for-py/pull/103>`_,
        `Py #105 <https://github.com/DoubleML/doubleml-for-py/pull/105>`_,
        `Py #106 <https://github.com/DoubleML/doubleml-for-py/pull/106>`_,
        `Py #111 <https://github.com/DoubleML/doubleml-for-py/pull/111>`_ &
        `Py #113 <https://github.com/DoubleML/doubleml-for-py/pull/113>`_

    .. dropdown:: DoubleML 0.2.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - IIVM model: Added a subgroups option to adapt to cases with and without the subgroups of always-takers and
        never-takers (`Py #96 <https://github.com/DoubleML/doubleml-for-py/pull/96>`_).
      - Add checks for the intersections of ``y_col``, ``d_cols``, ``x_cols``, ``z_cols``
        (`Py #84 <https://github.com/DoubleML/doubleml-for-py/issues/84>`_,
        `Py #97 <https://github.com/DoubleML/doubleml-for-py/pull/97>`_).
        This also fixes `Py #83 <https://github.com/DoubleML/doubleml-for-py/issues/83>`_ (with intersection
        between ``x_cols`` and ``d_cols`` a column could have been added multiple times to the covariate matrix).
      - Added checks and exception handling for duplicate entries in ``d_cols``, ``x_cols`` or ``z_cols``
        (`Py #100 <https://github.com/DoubleML/doubleml-for-py/pull/100>`_).
      - Check the datatype of ``data`` when initializing ``DoubleMLData`` objects. Also check for duplicate column names
        (`Py #100 <https://github.com/DoubleML/doubleml-for-py/pull/100>`_).
      - Fix bug `Py #95 <https://github.com/DoubleML/doubleml-for-py/issues/95>`_
        in `Py #97 <https://github.com/DoubleML/doubleml-for-py/pull/97>`_: It occurred when ``x_cols`` where inferred via
        setdiff and ``y_col`` was a string with multiple characters.
      - We updated the citation info to refer to the arXiv paper
        (`Py #98 <https://github.com/DoubleML/doubleml-for-py/pull/98>`_):
        Bach, P., Chernozhukov, V., Kurz, M. S., and Spindler, M. (2021), DoubleML - An Object-Oriented Implementation of
        Double Machine Learning in Python, `arXiv:2104.03220 <https://arxiv.org/abs/2104.03220>`_.

    .. dropdown:: DoubleML 0.2.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Provide an option to store & export the first-stage predictions
        `Py #91 <https://github.com/DoubleML/doubleml-for-py/pull/91>`_
      - Added the package logo to the doc

    .. dropdown:: DoubleML 0.2.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Major extensions of the unit test framework which result in a coverage >98% (a summary is given in
        `Py #82 <https://github.com/DoubleML/doubleml-for-py/pull/82>`_)
      - In the PLR one can now also specify classifiers for ``ml_m`` in case of a binary treatment variable with values 0
        and 1 (see `Py #86 <https://github.com/DoubleML/doubleml-for-py/pull/86>`_ for details)
      - The joint Python and R docu and user guide is now served to
        `https://docs.doubleml.org <https://docs.doubleml.org>`_ from a separate repo
        `https://github.com/DoubleML/doubleml-docs <https://github.com/DoubleML/doubleml-docs>`_
      - Generate and upload a unit test coverage report to codecov
        `https://app.codecov.io/gh/DoubleML/doubleml-for-py <https://app.codecov.io/gh/DoubleML/doubleml-for-py>`_
        `Py #76 <https://github.com/DoubleML/doubleml-for-py/pull/76>`_
      - Run lint checks with flake8 `Py #78 <https://github.com/DoubleML/doubleml-for-py/pull/78>`_, align code with PEP8
        standards `Py #79 <https://github.com/DoubleML/doubleml-for-py/pull/79>`_, activate code quality checks at codacy
        `Py #80 <https://github.com/DoubleML/doubleml-for-py/pull/80>`_
      - Refactoring (reduce code redundancy) of the code for tuning of the ML learners used for approximation the
        nuisance functions `Py #81 <https://github.com/DoubleML/doubleml-for-py/pull/81>`_
      - Minor updates, bug fixes and improvements of the exception handling
        (contained in `Py #82 <https://github.com/DoubleML/doubleml-for-py/pull/82>`_ &
        `Py #89 <https://github.com/DoubleML/doubleml-for-py/pull/89>`_)

    .. dropdown:: DoubleML 0.1.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - Fixed a compatibility issue with ``scikit-learn`` 0.24, which only affected some unit tests
        (`Py #70 <https://github.com/DoubleML/doubleml-for-py/issues/70>`_, `Py #71 <https://github.com/DoubleML/doubleml-for-py/pull/71>`_)
      - Added scheduled unit tests on github-action (three times a week) `Py #69 <https://github.com/DoubleML/doubleml-for-py/pull/69>`_
      - Split up estimation of nuisance functions and computation of score function components. Further introduced a
        private method ``_est_causal_pars_and_se()``, see `Py #72 <https://github.com/DoubleML/doubleml-for-py/pull/72>`_.
        This is needed for the DoubleML-Serverless project: https://github.com/DoubleML/doubleml-serverless.

    .. dropdown:: DoubleML 0.1.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Bug fix in the drawing of bootstrap weights for the multiple treatment case
        `Py #66 <https://github.com/DoubleML/doubleml-for-py/pull/66>`_ (see also https://github.com/DoubleML/doubleml-for-r/pull/28)
      - Update install instructions as DoubleML is now listed on pypi
      - Prepare submission to conda-forge: Include LICENSE file in source distribution
      - Documentation is now served with HTTPS `https://docs.doubleml.org/ <https://docs.doubleml.org/>`_

    .. dropdown:: DoubleML 0.1.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Initial release
      - Development at `https://github.com/DoubleML/doubleml-for-py <https://github.com/DoubleML/doubleml-for-py>`_
      - The Python package **DoubleML** provides an implementation of the double / debiased machine learning framework of
        `Chernozhukov et al. (2018) <https://doi.org/10.1111/ectj.12097)>`_.
      - Implements double machine learning for four different models:

        - Partially linear regression models (PLR) in class ``DoubleMLPLR``
        - Partially linear IV regression models (PLIV) in class ``DoubleMLPLIV``
        - Interactive regression models (IRM) in class ``DoubleMLIRM``
        - Interactive IV regression models (IIVM) in class ``DoubleMLIIVM``

      - All model classes are inherited from an abstract base class ``DoubleML`` where the key elements of double machine
        learning are implemented.

  .. tab-item:: R

    .. dropdown:: DoubleML 1.0.2
      :class-title: sd-bg-primary sd-font-weight-bold
      :open:

      - Add sample selection models, thanks to new contributor Petra Jasenakova `@petronelaj <https://github.com/petronelaj>`_
        `R #213 <https://github.com/DoubleML/doubleml-for-r/pull/213>`_
        `Docs #223 <https://github.com/DoubleML/doubleml-docs/pull/223>`_
      - Maintenance including updates to GitHub workflows
        `R #205 <https://github.com/DoubleML/doubleml-for-r/pull/205>`_
        `R #220 <https://github.com/DoubleML/doubleml-for-r/pull/220>`_
        `Docs #226 <https://github.com/DoubleML/doubleml-docs/pull/226>`_

    .. dropdown:: DoubleML 1.0.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Maintenance (upcoming breaking changes from ``paradox`` package), thanks to new contributor Martin Binder `@mb706 <https://github.com/mb706>`_
        `R #195 <https://github.com/DoubleML/doubleml-for-r/pull/195>`_
        `R #198 <https://github.com/DoubleML/doubleml-for-r/pull/199>`_

    .. dropdown:: DoubleML 1.0.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Update citation info to publication in Journal of Statistical Software, rename helper function and fix links and GH actions
        `R #191 <https://github.com/DoubleML/doubleml-for-r/pull/191>`_

    .. dropdown:: DoubleML 0.5.3
      :class-title: sd-bg-primary sd-font-weight-bold

      - Add documentation for estimated models for nuisance parameters
        `R #181 <https://github.com/DoubleML/doubleml-for-r/pull/181>`_
      - New contributor `@SvenKlaassen <https://github.com/SvenKlaassen>`_
      - Maintenance
        `R #179 <https://github.com/DoubleML/doubleml-for-r/pull/179>`_

    .. dropdown:: DoubleML 0.5.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - Store estimated models for nuisance parameters
        `R #169 <https://github.com/DoubleML/doubleml-for-r/pull/169>`_
      - New maintainer of the CRAN package DoubleML `@PhilippBach <https://github.com/PhilippBach>`_
      - Maintenance
        `R #170 <https://github.com/DoubleML/doubleml-for-r/pull/170>`_
        `R #173 <https://github.com/DoubleML/doubleml-for-r/pull/173>`_
        `R #174 <https://github.com/DoubleML/doubleml-for-r/pull/174>`_
        `R #177 <https://github.com/DoubleML/doubleml-for-r/pull/177>`_
        `R #178 <https://github.com/DoubleML/doubleml-for-r/pull/178>`_

    .. dropdown:: DoubleML 0.5.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Fix a CRAN issue (html checks) by regenerating ``.Rd``-files with the newest version of ``roxygen2``.
        `R #166 <https://github.com/DoubleML/doubleml-for-r/issues/166>`_
        `R #167 <https://github.com/DoubleML/doubleml-for-r/pull/167>`_
        `R #168 <https://github.com/DoubleML/doubleml-for-r/pull/168>`_

    .. dropdown:: DoubleML 0.5.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Implement a new score function ``score = 'IV-type'`` for the PLIV model (for details see
        `R #161 <https://github.com/DoubleML/doubleml-for-r/pull/161>`_) |br|
        --> **API change** from ``DoubleMLPLIV$new(obj_dml_data, ml_g, ml_m, ml_r [, ...])``
        to ``DoubleMLPLIV$new(obj_dml_data, ml_g, ml_m, ml_r, ml_g [, ...])``
      - Adapt the nuisance estimation for the ``'IV-type'`` score for the PLR model (for details see
        `R #161 <https://github.com/DoubleML/doubleml-for-r/pull/161>`_) |br|
        --> **API change** from ``DoubleMLPLR$new(obj_dml_data, ml_g, ml_m [, ...])``
        to ``DoubleMLPLR$new(obj_dml_data, ml_l, ml_m, ml_g [, ...])``
      - Use ``task_type`` instead of ``learner_class`` to identify whether a learner is meant to regress or classify (this
        change makes it possible to easily integrate pipelines from ``mlr3pipelines`` as learner for the nuisance functions)
        `R #141 <https://github.com/DoubleML/doubleml-for-r/pull/141>`_
      - Add `R Contribution Guidelines <https://github.com/DoubleML/doubleml-for-r/blob/main/CONTRIBUTING.md>`_,
        issue templates, a pull request template and a
        `R discussion forum <https://github.com/DoubleML/doubleml-for-r/discussions>`_ to the R package repository
        `R #142 <https://github.com/DoubleML/doubleml-for-r/pull/142>`_
        `R #146 <https://github.com/DoubleML/doubleml-for-r/pull/146>`_
        `R #147 <https://github.com/DoubleML/doubleml-for-r/pull/147>`_
      - Allow the usage of classifiers for binary outcome variables in the model classes IRM and IIVM
        `R #114 <https://github.com/DoubleML/doubleml-for-r/pull/114>`_
      - Bug fixes and maintenance
        `R #155 <https://github.com/DoubleML/doubleml-for-r/issues/155>`_
        `R #156 <https://github.com/DoubleML/doubleml-for-r/issues/156>`_
        `R #157 <https://github.com/DoubleML/doubleml-for-r/issues/157>`_
        `R #158 <https://github.com/DoubleML/doubleml-for-r/issues/158>`_
        `R #160 <https://github.com/DoubleML/doubleml-for-r/pull/160>`_
        `R #163 <https://github.com/DoubleML/doubleml-for-r/pull/163>`_

    .. dropdown:: DoubleML 0.4.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Prevent usage of ``glmnet`` learner for unit testing as recommended by CRAN (failing tests on Solaris)
        `R #137 <https://github.com/DoubleML/doubleml-for-r/pull/137>`_
      - Prepare for the upcoming release of ``checkmate`` which is not backward compatible with our unit tests
        `R #134 <https://github.com/DoubleML/doubleml-for-r/pull/134>`_

    .. dropdown:: DoubleML 0.4.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Clustered standard errors for double machine learning models
        `R #119 <https://github.com/DoubleML/doubleml-for-r/pull/119>`_
      - Apply styler as described in the wiki (https://github.com/DoubleML/doubleml-for-r/wiki/Style-Guidelines) and add a
        corresponding CI on github actions `R #120 <https://github.com/DoubleML/doubleml-for-r/pull/120>`_
        `R #122 <https://github.com/DoubleML/doubleml-for-r/pull/122>`_
      - Other refactoring, bug fixes and documentation updates
        `R #127 <https://github.com/DoubleML/doubleml-for-r/pull/127>`_
        `R #129 <https://github.com/DoubleML/doubleml-for-r/pull/129>`_
        `R #130 <https://github.com/DoubleML/doubleml-for-r/pull/130>`_
        `R #131 <https://github.com/DoubleML/doubleml-for-r/pull/131>`_
        `R #132 <https://github.com/DoubleML/doubleml-for-r/pull/132>`_
        `R #133 <https://github.com/DoubleML/doubleml-for-r/pull/133>`_

    .. dropdown:: DoubleML 0.3.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Initialize all numeric matrices, vectors and arrays with the correct data type by using ``NA_real_`` instead of
        ``NA`` and replace a ``print()`` call with ``cat()`` `R #115 <https://github.com/DoubleML/doubleml-for-r/pull/115>`_

    .. dropdown:: DoubleML 0.3.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Use active bindings in the R6 OOP implementation
        `R #106 <https://github.com/DoubleML/doubleml-for-r/pull/106>`_ &
        `R #93 <https://github.com/DoubleML/doubleml-for-r/issues/93>`_
      - Fix the aggregation formula for standard errors from repeated cross-fitting
        `R #94 <https://github.com/DoubleML/doubleml-for-r/issues/94>`_ &
        `R #95 <https://github.com/DoubleML/doubleml-for-r/pull/95>`_
      - Always use the same bootstrap algorithm independent of ``dml1`` vs ``dml2`` and consistent with docu and paper
        `R #98 <https://github.com/DoubleML/doubleml-for-r/issues/98>`_ &
        `R #99 <https://github.com/DoubleML/doubleml-for-r/pull/99>`_
      - Initialize predictions with NA and make sure that there are no misleading entries in the evaluated score
        functions `R #96 <https://github.com/DoubleML/doubleml-for-r/issues/96>`_ &
        `R #105 <https://github.com/DoubleML/doubleml-for-r/pull/105>`_
      - Avoid overriding learner parameters during tuning
        `R #83 <https://github.com/DoubleML/doubleml-for-r/issues/83>`_ &
        `R #84 <https://github.com/DoubleML/doubleml-for-r/pull/84>`_
      - Fixes in the exception handling and extension of the unit tests for the score function choice
        `R #82 <https://github.com/DoubleML/doubleml-for-r/pull/82>`_
      - Prevent overwriting parameters from initialization when calling set_ml_nuisance_params
        `R #87 <https://github.com/DoubleML/doubleml-for-r/issues/87>`_ &
        `R #89 <https://github.com/DoubleML/doubleml-for-r/pull/89>`_
      - Major refactoring and cleanup and extension of the unit test framework
        `R #101 <https://github.com/DoubleML/doubleml-for-r/pull/101>`_
      - Extension and reorganization of exception handling for ``DoubleMLData`` objects
        `R #63 <https://github.com/DoubleML/doubleml-for-r/issues/63>`_ &
        `R #90 <https://github.com/DoubleML/doubleml-for-r/pull/90>`_
      - Introduce style guide and clean up code
        `R #80 <https://github.com/DoubleML/doubleml-for-r/pull/80>`_ &
        `R #81 <https://github.com/DoubleML/doubleml-for-r/pull/81>`_
      - Adaption to be compatible with an API change in the next ``mlr3`` release
        `R #103 <https://github.com/DoubleML/doubleml-for-r/pull/103>`_
      - Run unit tests with mlr3 in dev version on github actions
        `R #104 <https://github.com/DoubleML/doubleml-for-r/pull/104>`_
      - Updated the citation info
        `R #78 <https://github.com/DoubleML/doubleml-for-r/pull/78>`_,
        `R #79 <https://github.com/DoubleML/doubleml-for-r/pull/79>`_ &
        `R #86 <https://github.com/DoubleML/doubleml-for-r/pull/86>`_
      - Added a short version of and a reference to the arXiv paper as vignette
        `R #110 <https://github.com/DoubleML/doubleml-for-r/pull/110>`_ &
        `R #113 <https://github.com/DoubleML/doubleml-for-r/issues/113>`_
      - Prevent using the subclassed methods check_score and check_data when constructing DoubleML objects
        `R #107 <https://github.com/DoubleML/doubleml-for-r/pull/107>`_
      - Other refactoring and minor adaptions
        `R #91 <https://github.com/DoubleML/doubleml-for-r/pull/91>`_,
        `R #92 <https://github.com/DoubleML/doubleml-for-r/pull/92>`_,
        `R #102 <https://github.com/DoubleML/doubleml-for-r/pull/102>`_ &
        `R #108 <https://github.com/DoubleML/doubleml-for-r/pull/108>`_

    .. dropdown:: DoubleML 0.2.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Provide an option to store & export the first-stage predictions
        `R #74 <https://github.com/DoubleML/doubleml-for-r/pull/74>`_
      - Reduce and refine messaging to the console during estimation
        `R #72 <https://github.com/DoubleML/doubleml-for-r/pull/72>`_
      - Fix bug in IIVM model if the IV variable is not named ``z``
        `R #75 <https://github.com/DoubleML/doubleml-for-r/pull/75>`_
      - Fix failing unit test `R #71 <https://github.com/DoubleML/doubleml-for-r/pull/71>`_
      - Added the package logo to the doc

    .. dropdown:: DoubleML 0.2.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - In the PLR one can now also specify classifiers for ``ml_m`` in case of a binary treatment variable with values 0 and 1
      - Major refactoring of core-parts of the estimation and tuning of the ML estimators for the nuisance functions: All models now use central helper functions ``dml_cv_predict()`` and ``dml_tune()``
      - Extensions to the unit test framework to improve upon test coverage
      - Added unit test coverage via codecov: `https://app.codecov.io/gh/DoubleML/doubleml-for-r <https://app.codecov.io/gh/DoubleML/doubleml-for-r>`_
      - Minor docu updates and adaptions: `R #58 <https://github.com/DoubleML/doubleml-for-r/pull/58>`_, `R #61 <https://github.com/DoubleML/doubleml-for-r/pull/61>`_ & `R #70 <https://github.com/DoubleML/doubleml-for-r/pull/70>`_

    .. dropdown:: DoubleML 0.1.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - Adapt calls to ``mlr3tuning`` due to a change in their API (since version 0.6.0): fixes `R #51 <https://github.com/DoubleML/doubleml-for-r/issues/51>`_
      - Add ``bbotk`` to suggests: fixes R CMD check note `R #47 <https://github.com/DoubleML/doubleml-for-r/issues/47>`_
      - Use ``doi{}`` command: fixes R CMD check note `R #54 <https://github.com/DoubleML/doubleml-for-r/issues/54>`_
      - Minor docu updates as ``DoubleML`` is now available on CRAN

    .. dropdown:: DoubleML 0.1.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - First release to CRAN `https://cran.r-project.org/package=DoubleML <https://cran.r-project.org/package=DoubleML>`_
      - Clean up of imports
      - Continuous integration was extended by unit tests on github actions
        `https://github.com/DoubleML/doubleml-for-r/actions <https://github.com/DoubleML/doubleml-for-r/actions>`_

    .. dropdown:: DoubleML 0.1.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Initial release
      - Development at `https://github.com/DoubleML/doubleml-for-r <https://github.com/DoubleML/doubleml-for-r>`_
      - The R package **DoubleML** provides an implementation of the double / debiased machine learning framework of
        `Chernozhukov et al. (2018) <https://doi.org/10.1111/ectj.12097)>`_.
      - Implements double machine learning for four different models:

        - Partially linear regression models (PLR) in class ``DoubleMLPLR``
        - Partially linear IV regression models (PLIV) in class ``DoubleMLPLIV``
        - Interactive regression models (IRM) in class ``DoubleMLIRM``
        - Interactive IV regression models (IIVM) in class ``DoubleMLIIVM``

      - All model classes are inherited from ``DoubleML`` where the key elements of double machine learning are
        implemented.

.. |br| raw:: html

  <br/>
