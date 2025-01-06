:parenttoc: True

Release notes
=============

.. tab-set::

  .. tab-item:: Python

    .. dropdown:: DoubleML 0.9.1
      :class-title: sd-bg-primary sd-font-weight-bold
      :open:

      - **Release highlight:** Regression Discontinuity Designs with Flexible Covariate Adjustment
        via ``RDFlex`` class (in cooperation with `Claudia Noack <https://github.com/claudianoack>`_
        and `Tomasz Olma <https://github.com/tomaszolma>`_; see `their paper` <https://arxiv.org/abs/2107.07942>`_)
        `#276 <https://github.com/DoubleML/doubleml-for-py/pull/276>`_

      - Add ``cov_type=HC0`` and enable key-worded arguments to ``DoubleMLBLP``
        `#270 <https://github.com/DoubleML/doubleml-for-py/issues/270>`_
        `#271 <https://github.com/DoubleML/doubleml-for-py/pull/271>`_

      - Update User Guide and Example Gallery
        `#204 <https://github.com/DoubleML/doubleml-docs/pull/204>`_

      - Add AutoML example for tuning DoubleML estimators
        `#199 <https://github.com/DoubleML/doubleml-docs/pull/199>`_

      - Maintainance package
        `#268 <https://github.com/DoubleML/doubleml-for-py/pull/268>`_
        `#278 <https://github.com/DoubleML/doubleml-for-py/issues/278>`
        `#279 <https://github.com/DoubleML/doubleml-for-py/pull/279>`
        `#281 <https://github.com/DoubleML/doubleml-for-py/pull/281>`
        `#282 <https://github.com/DoubleML/doubleml-for-py/pull/282>` 

      - Maintenance documentation
        `#201 <https://github.com/DoubleML/doubleml-docs/pull/201>`_
        `#203 <https://github.com/DoubleML/doubleml-docs/pull/203>`_

    .. dropdown:: DoubleML 0.9.0
      :class-title: sd-bg-primary sd-font-weight-bold
      :open:

      - **Release highlight:** Average potential outcomes for multiple discrete treatments
        via ``DoubleMLAPO`` and ``DoubleMLAPOS`` classes (proposed by `Apoorva Lal <https://github.com/apoorvalal>`_)
        `#245 <https://github.com/DoubleML/doubleml-for-py/issues/245>`_
        `#250 <https://github.com/DoubleML/doubleml-for-py/pull/250>`_

      - Update User Guide and Example Gallery
        `#188 <https://github.com/DoubleML/doubleml-docs/pull/188>`_
        `#195 <https://github.com/DoubleML/doubleml-docs/pull/195>`_

      - Add sensitivity analysis to ``DoubleMLFramework``
        `#249 <https://github.com/DoubleML/doubleml-for-py/pull/249>`_

      - Maintainance package
        `#264 <https://github.com/DoubleML/doubleml-for-py/pull/264>`_
        `#265 <https://github.com/DoubleML/doubleml-for-py/pull/265>`_
        `#266 <https://github.com/DoubleML/doubleml-for-py/pull/266>`_

      - Maintenance documentation
        `#182 <https://github.com/DoubleML/doubleml-docs/pull/182>`_
        `#184 <https://github.com/DoubleML/doubleml-docs/pull/184>`_
        `#186 <https://github.com/DoubleML/doubleml-docs/pull/186>`_
        `#193 <https://github.com/DoubleML/doubleml-docs/pull/193>`_
        `#194 <https://github.com/DoubleML/doubleml-docs/pull/194>`_
        `#196 <https://github.com/DoubleML/doubleml-docs/pull/196>`_
        `#197 <https://github.com/DoubleML/doubleml-docs/pull/197>`_

    .. dropdown:: DoubleML 0.8.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - **API Update**: Change nuisance evaluation for classifiers.
        The corresponding properties are renamed ``nuisance_loss`` instead of ``rmses``.
        `#254 <https://github.com/DoubleML/doubleml-for-py/pull/254>`_
        `#184 <https://github.com/DoubleML/doubleml-docs/pull/184>`_

      - Add new example on sensitivity analysis
        `#190 <https://github.com/DoubleML/doubleml-docs/pull/190>`_

      - Add a new example on DiD with DoubleML in R
        `#178 <https://github.com/DoubleML/doubleml-docs/pull/178>`_

      - Enable ``set_sample_splitting`` for cluster data
        `#255 <https://github.com/DoubleML/doubleml-for-py/pull/255>`_

      - Update the ``make_confounded_irm_data`` data generating process
        `#263 <https://github.com/DoubleML/doubleml-for-py/pull/263>`_
      
      - Maintainance package
        `#264 <https://github.com/DoubleML/doubleml-for-py/pull/264>`_

      - Maintenance documentation
        `#177 <https://github.com/DoubleML/doubleml-docs/pull/177>`_
        `#180 <https://github.com/DoubleML/doubleml-docs/pull/180>`_
        `#181 <https://github.com/DoubleML/doubleml-docs/pull/181>`_
        `#187 <https://github.com/DoubleML/doubleml-docs/pull/187>`_
        `#189 <https://github.com/DoubleML/doubleml-docs/pull/189>`_

    .. dropdown:: DoubleML 0.8.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Increment package requirements and update workflows for python 3.9 (add tests for python 3.12)
        `#247 <https://github.com/DoubleML/doubleml-for-py/pull/247>`_
        `#175 <https://github.com/DoubleML/doubleml-docs/pull/175>`_

      - Additional example for ranking treatment effects (by `Apoorva Lal <https://github.com/apoorvalal>`_)
        `#173 <https://github.com/DoubleML/doubleml-docs/pull/173>`_
        `#174 <https://github.com/DoubleML/doubleml-docs/pull/174>`_

      - Maintainance documentation
        `#172 <https://github.com/DoubleML/doubleml-docs/pull/172>`_

    .. dropdown:: DoubleML 0.8.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Sample-selections models as ``DoubleMLSMM`` class (by `Michaela Kecskésová <https://github.com/mychaelka>`_)
        `#231 <https://github.com/DoubleML/doubleml-for-py/pull/231>`_
        `#235 <https://github.com/DoubleML/doubleml-for-py/pull/235>`_
        `#171 <https://github.com/DoubleML/doubleml-docs/pull/171>`_
      - **API change:** Remove options ``apply_crossfitting`` and ``dml_procedure`` from the ``DoubleML`` class
        `#227 <https://github.com/DoubleML/doubleml-for-py/pull/227>`_
        `#166 <https://github.com/DoubleML/doubleml-docs/pull/166>`_
      - Restructure the package to improve readability and maintainability
        `#225 <https://github.com/DoubleML/doubleml-for-py/pull/225>`_
      - Add a ``DoubleMLFramework`` class to combine multiple DoubleML models (aggregation of estimates, boostrap and CI-procedures)
        `#226 <https://github.com/DoubleML/doubleml-for-py/pull/226>`_
        `#169 <https://github.com/DoubleML/doubleml-docs/pull/169>`_
      - Enable the use of external predictions for short models in benchmarks (by `Lucien <https://github.com/lucien1011>`_)
        `#238 <https://github.com/DoubleML/doubleml-for-py/pull/238>`_
        `#239 <https://github.com/DoubleML/doubleml-for-py/pull/239>`_
      - Add the ``gain_statistics`` to ``utils`` to sensitivity analysis
        `#229 <https://github.com/DoubleML/doubleml-for-py/pull/229>`_

      - Maintenance documentation
        `#162 <https://github.com/DoubleML/doubleml-docs/pull/162>`_
        `#163 <https://github.com/DoubleML/doubleml-docs/pull/163>`_
        `#164 <https://github.com/DoubleML/doubleml-docs/pull/164>`_
        `#165 <https://github.com/DoubleML/doubleml-docs/pull/165>`_
        `#167 <https://github.com/DoubleML/doubleml-docs/pull/167>`_
        `#168 <https://github.com/DoubleML/doubleml-docs/pull/168>`_

      - Maintainance package
        `#225 <https://github.com/DoubleML/doubleml-for-py/pull/225>`_
        `#229 <https://github.com/DoubleML/doubleml-for-py/pull/229>`_
        `#246 <https://github.com/DoubleML/doubleml-for-py/pull/246>`_

    .. dropdown:: DoubleML 0.7.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Add weights to ``DoubleMLIRM`` class to extend sensitivity to GATEs etc.
        `#220 <https://github.com/DoubleML/doubleml-for-py/pull/220>`_
        `#229 <https://github.com/DoubleML/doubleml-for-py/pull/229>`_
        `#155 <https://github.com/DoubleML/doubleml-docs/pull/155>`_
        `#161 <https://github.com/DoubleML/doubleml-docs/pull/161>`_
      - Extend GATE and CATE estimation to the ``DoubleMLPLR`` class
        `#220 <https://github.com/DoubleML/doubleml-for-py/pull/220>`_
        `#155 <https://github.com/DoubleML/doubleml-docs/pull/155>`_
      - Enable the use of external predictions for ``DoubleML`` classes
        `#221 <https://github.com/DoubleML/doubleml-for-py/pull/221>`_
        `#159 <https://github.com/DoubleML/doubleml-docs/pull/159>`_

      - Implementing utility classes and functions (gain statistics and dummy learners)
        `#221 <https://github.com/DoubleML/doubleml-for-py/pull/221>`_
        `#222 <https://github.com/DoubleML/doubleml-for-py/pull/222>`_
        `#229 <https://github.com/DoubleML/doubleml-for-py/pull/229>`_
        `#161 <https://github.com/DoubleML/doubleml-docs/pull/161>`_

      - Extend example Gallery
        `#153 <https://github.com/DoubleML/doubleml-docs/pull/153>`_
        `#158 <https://github.com/DoubleML/doubleml-docs/pull/158>`_
        `#161 <https://github.com/DoubleML/doubleml-docs/pull/161>`_

      - Maintenance documentation
        `#157 <https://github.com/DoubleML/doubleml-docs/pull/157>`_
        `#160 <https://github.com/DoubleML/doubleml-docs/pull/160>`_

      - Maintenance package
        `#223 <https://github.com/DoubleML/doubleml-for-py/pull/223>`_
        `#224 <https://github.com/DoubleML/doubleml-for-py/pull/224>`_


    .. dropdown:: DoubleML 0.7.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Benchmarking for Sensitivity Analysis (omitted variable bias)
        `#211 <https://github.com/DoubleML/doubleml-for-py/pull/211>`_
      - Policy tree estimation for the ``DoubleMLIRM`` class
        `#212 <https://github.com/DoubleML/doubleml-for-py/pull/212>`_

      - Extending sensitivity and policy tree documentation in User Guide and Example Gallery
        `#148 <https://github.com/DoubleML/doubleml-docs/pull/148>`_
        `#150 <https://github.com/DoubleML/doubleml-docs/pull/150>`_

      - The package requirements are set to python 3.8 or higher
        `#211 <https://github.com/DoubleML/doubleml-for-py/pull/211>`_
      
      - Maintenance documentation
        `#149 <https://github.com/DoubleML/doubleml-docs/pull/149>`_
      - Maintenance package
        `#213 <https://github.com/DoubleML/doubleml-for-py/pull/213>`_

    .. dropdown:: DoubleML 0.6.3
      :class-title: sd-bg-primary sd-font-weight-bold

      - Fix install requirements for 0.6.2
        `#208 <https://github.com/DoubleML/doubleml-for-py/pull/208>`_

    .. dropdown:: DoubleML 0.6.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Sensitivity Analysis (omitted variable bias) for
        `#201 <https://github.com/DoubleML/doubleml-for-py/pull/201>`_

        - ``DoubleMLPLR``
        - ``DoubleMLIRM``
        - ``DoubleMLDID``
        - ``DoubleMLDIDCS``
      
      - Updated documentation
        `#144 <https://github.com/DoubleML/doubleml-docs/pull/144>`_
        `#141 <https://github.com/DoubleML/doubleml-docs/pull/141>`_

      - Extend the guide with sensitivity and add further examples
        `#142 <https://github.com/DoubleML/doubleml-docs/pull/142>`_

      - Maintenance package
        `#202 <https://github.com/DoubleML/doubleml-for-py/pull/202>`_
        `#206 <https://github.com/DoubleML/doubleml-for-py/pull/206>`_

      - Maintenance documentation
        `#137 <https://github.com/DoubleML/doubleml-docs/pull/137>`_
        `#138 <https://github.com/DoubleML/doubleml-docs/pull/138>`_
        `#140 <https://github.com/DoubleML/doubleml-docs/pull/140>`_
        `#143 <https://github.com/DoubleML/doubleml-docs/pull/143>`_
        `#145 <https://github.com/DoubleML/doubleml-docs/pull/145>`_
        `#146 <https://github.com/DoubleML/doubleml-docs/pull/146>`_

    .. dropdown:: DoubleML 0.6.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Difference-in-differences models for ATTE estimation
        `#200 <https://github.com/DoubleML/doubleml-for-py/pull/200>`_
        `#194 <https://github.com/DoubleML/doubleml-for-py/issues/194>`_

        - Panel data ``DoubleMLDID``
        - Repeated cross sections ``DoubleMLDIDCS``
      
      - Add a potential time variable to ``DoubleMLData`` (until now only used in ``DoubleMLDIDCS``)
        `#200 <https://github.com/DoubleML/doubleml-for-py/pull/200>`_

      - Extend the guide in the documentation and add further examples
        `#132 <https://github.com/DoubleML/doubleml-docs/pull/132>`_
        `#133 <https://github.com/DoubleML/doubleml-docs/pull/133>`_
        `#135 <https://github.com/DoubleML/doubleml-docs/pull/135>`_

      - Maintenance
        `#199 <https://github.com/DoubleML/doubleml-for-py/pull/199>`_
        `#134 <https://github.com/DoubleML/doubleml-docs/pull/134>`_
        `#136 <https://github.com/DoubleML/doubleml-docs/pull/136>`_  

    .. dropdown:: DoubleML 0.6.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Heterogeneous treatment effects (GATE, CATE, Quantile effects, ...)
      - Add out-of-sample RMSE and targets for nuisance elements and implement nuisance estimation 
        evaluation via ``evaluate_learners()``.
        `#182 <https://github.com/DoubleML/doubleml-for-py/pull/182>`_
        `#188 <https://github.com/DoubleML/doubleml-for-py/pull/188>`_
      - Implement ``gate()`` and ``cate()`` methods for ``DoubleMLIRM`` class. Both are 
        based on the new ``DoubleMLBLP`` class.
        `#169 <https://github.com/DoubleML/doubleml-for-py/pull/169>`_
      - Implement different type of quantile models
        `#179 <https://github.com/DoubleML/doubleml-for-py/pull/179>`_
        
        - Potential quantiles (PQ) in class ``DoubleMLPQ``
        - Local potential quantiles (LPQ) in class ``DoubleMLLPQ``
        - Conditional value at risk (CVaR) in class ``DoubleMLCVAR``
        - Quantile treatment effects (QTE) in class ``DoubleMLQTE``

      - Extend clustering to nonlinear scores
        `#190 <https://github.com/DoubleML/doubleml-for-py/pull/190>`_
      - Add ``ipw_normalization`` option to ``DoubleMLIRM`` and ``DoubleMLIIVM``
        `#186 <https://github.com/DoubleML/doubleml-for-py/pull/186>`_
      - Implement an abstract base class for data backends 
        `#173 <https://github.com/DoubleML/doubleml-for-py/pull/173>`_
      - Extend the guide in the documentation and add further examples
        `#116 <https://github.com/DoubleML/doubleml-docs/pull/116>`_
        `#125 <https://github.com/DoubleML/doubleml-docs/pull/125>`_
        `#126 <https://github.com/DoubleML/doubleml-docs/pull/126>`_
      - Code refactorings, bug fixes, docu updates, unit test extensions and continuous integration
        `#183 <https://github.com/DoubleML/doubleml-for-py/pull/183>`_
        `#192 <https://github.com/DoubleML/doubleml-for-py/pull/192>`_
        `#195 <https://github.com/DoubleML/doubleml-for-py/pull/195>`_
        `#196 <https://github.com/DoubleML/doubleml-for-py/pull/196>`_
      - Change License to BSD 3-Clause
        `#198 <https://github.com/DoubleML/doubleml-for-py/pull/198>`_
      - Maintenance
        `#174 <https://github.com/DoubleML/doubleml-for-py/pull/174>`_
        `#178 <https://github.com/DoubleML/doubleml-for-py/pull/178>`_
        `#181 <https://github.com/DoubleML/doubleml-for-py/pull/181>`_

    .. dropdown:: DoubleML 0.5.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - Fix / adapted unit tests which failed in the release of 0.5.1 to conda-forge
        `#172 <https://github.com/DoubleML/doubleml-for-py/pull/172>`_

    .. dropdown:: DoubleML 0.5.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Store estimated models for nuisance parameters
        `#159 <https://github.com/DoubleML/doubleml-for-py/pull/159>`_
      - Bug fix: Overwrite for tune method (introduced for depreciation warning) did not return the tune result
        `#160 <https://github.com/DoubleML/doubleml-for-py/pull/160>`_
        `#162 <https://github.com/DoubleML/doubleml-for-py/issues/162>`_
      - Maintenance
        `#166 <https://github.com/DoubleML/doubleml-for-py/pull/166>`_
        `#167 <https://github.com/DoubleML/doubleml-for-py/pull/167>`_
        `#168 <https://github.com/DoubleML/doubleml-for-py/pull/168>`_
        `#170 <https://github.com/DoubleML/doubleml-for-py/pull/170>`_

    .. dropdown:: DoubleML 0.5.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Implement a new score function ``score = 'IV-type'`` for the PLIV model (for details see
        `#151 <https://github.com/DoubleML/doubleml-for-py/pull/151>`_) |br|
        --> **API change** from ``DoubleMLPLIV(obj_dml_data, ml_g, ml_m, ml_r [, ...])``
        to ``DoubleMLPLIV(obj_dml_data, ml_g, ml_m, ml_r, ml_g [, ...])``
      - Adapt the nuisance estimation for the ``'IV-type'`` score for the PLR model (for details see
        `#151 <https://github.com/DoubleML/doubleml-for-py/pull/151>`_) |br|
        --> **API change** from ``DoubleMLPLR(obj_dml_data, ml_g, ml_m [, ...])``
        to ``DoubleMLPLR(obj_dml_data, ml_l, ml_m, ml_g [, ...])``
      - Allow the usage of classifiers for binary outcome variables in the model classes IRM and IIVM
        `#134 <https://github.com/DoubleML/doubleml-for-py/pull/134>`_
      - **Published in JMLR: DoubleML - An Object-Oriented Implementation of Double Machine Learning in Python** (citation
        info updated in `#138 <https://github.com/DoubleML/doubleml-for-py/pull/138>`_)
      - Maintenance
        `#143 <https://github.com/DoubleML/doubleml-for-py/pull/143>`_
        `#148 <https://github.com/DoubleML/doubleml-for-py/pull/148>`_
        `#149 <https://github.com/DoubleML/doubleml-for-py/pull/149>`_
        `#152 <https://github.com/DoubleML/doubleml-for-py/issues/152>`_
        `#153 <https://github.com/DoubleML/doubleml-for-py/pull/153>`_

    .. dropdown:: DoubleML 0.4.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - We added `Contribution Guidelines <https://github.com/DoubleML/doubleml-for-py/blob/main/CONTRIBUTING.md>`_,
        issue templates, a pull request template and a
        `discussion forum <https://github.com/DoubleML/doubleml-for-py/discussions>`_ to the Python package repository
        `#132 <https://github.com/DoubleML/doubleml-for-py/pull/132>`_
      - Code refactorings, docu updates, unit test extensions and continuous integration
        `#126 <https://github.com/DoubleML/doubleml-for-py/pull/126>`_
        `#127 <https://github.com/DoubleML/doubleml-for-py/pull/127>`_
        `#128 <https://github.com/DoubleML/doubleml-for-py/pull/128>`_
        `#130 <https://github.com/DoubleML/doubleml-for-py/pull/130>`_
        `#131 <https://github.com/DoubleML/doubleml-for-py/pull/131>`_

    .. dropdown:: DoubleML 0.4.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Clustered standard errors for double machine learning models
        `#116 <https://github.com/DoubleML/doubleml-for-py/pull/116>`_
      - Improve exception handling for missings and infinite values in the confounders, predictions, etc.
        (fixes `#120 <https://github.com/DoubleML/doubleml-for-py/issues/120>`_ by allowing null confounder values)
        `#122 <https://github.com/DoubleML/doubleml-for-py/pull/122>`_
      - Clean up dev requirements and use dev requirements on github actions
        `#121 <https://github.com/DoubleML/doubleml-for-py/pull/121>`_
      - Other updates
        `#123 <https://github.com/DoubleML/doubleml-for-py/pull/123>`_

    .. dropdown:: DoubleML 0.3.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Always use the same bootstrap algorithm independent of ``dml1`` vs ``dml2`` and consistent with docu and paper
        `#101 <https://github.com/DoubleML/doubleml-for-py/issues/101>`_ &
        `#102 <https://github.com/DoubleML/doubleml-for-py/pull/102>`_
      - Added an exception handling to assure that an IV variable is specified when using a PLIV or IIVM model
        `#107 <https://github.com/DoubleML/doubleml-for-py/pull/107>`_
      - Improve exception handling for externally provided sample splitting
        `#110 <https://github.com/DoubleML/doubleml-for-py/pull/110>`_
      - Minor update of the str representation of ``DoubleMLData`` objects
        `#112 <https://github.com/DoubleML/doubleml-for-py/pull/112>`_
      - Code refactorings and unit test extensions
        `#103 <https://github.com/DoubleML/doubleml-for-py/pull/103>`_,
        `#105 <https://github.com/DoubleML/doubleml-for-py/pull/105>`_,
        `#106 <https://github.com/DoubleML/doubleml-for-py/pull/106>`_,
        `#111 <https://github.com/DoubleML/doubleml-for-py/pull/111>`_ &
        `#113 <https://github.com/DoubleML/doubleml-for-py/pull/113>`_

    .. dropdown:: DoubleML 0.2.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - IIVM model: Added a subgroups option to adapt to cases with and without the subgroups of always-takers and
        never-takers (`#96 <https://github.com/DoubleML/doubleml-for-py/pull/96>`_).
      - Add checks for the intersections of ``y_col``, ``d_cols``, ``x_cols``, ``z_cols``
        (`#84 <https://github.com/DoubleML/doubleml-for-py/issues/84>`_,
        `#97 <https://github.com/DoubleML/doubleml-for-py/pull/97>`_).
        This also fixes `#83 <https://github.com/DoubleML/doubleml-for-py/issues/83>`_ (with intersection
        between ``x_cols`` and ``d_cols`` a column could have been added multiple times to the covariate matrix).
      - Added checks and exception handling for duplicate entries in ``d_cols``, ``x_cols`` or ``z_cols``
        (`#100 <https://github.com/DoubleML/doubleml-for-py/pull/100>`_).
      - Check the datatype of ``data`` when initializing ``DoubleMLData`` objects. Also check for duplicate column names
        (`#100 <https://github.com/DoubleML/doubleml-for-py/pull/100>`_).
      - Fix bug `#95 <https://github.com/DoubleML/doubleml-for-py/issues/95>`_
        in `#97 <https://github.com/DoubleML/doubleml-for-py/pull/97>`_: It occurred when ``x_cols`` where inferred via
        setdiff and ``y_col`` was a string with multiple characters.
      - We updated the citation info to refer to the arXiv paper
        (`#98 <https://github.com/DoubleML/doubleml-for-py/pull/98>`_):
        Bach, P., Chernozhukov, V., Kurz, M. S., and Spindler, M. (2021), DoubleML - An Object-Oriented Implementation of
        Double Machine Learning in Python, `arXiv:2104.03220 <https://arxiv.org/abs/2104.03220>`_.

    .. dropdown:: DoubleML 0.2.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Provide an option to store & export the first-stage predictions
        `#91 <https://github.com/DoubleML/doubleml-for-py/pull/91>`_
      - Added the package logo to the doc

    .. dropdown:: DoubleML 0.2.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Major extensions of the unit test framework which result in a coverage >98% (a summary is given in
        `#82 <https://github.com/DoubleML/doubleml-for-py/pull/82>`_)
      - In the PLR one can now also specify classifiers for ``ml_m`` in case of a binary treatment variable with values 0
        and 1 (see `#86 <https://github.com/DoubleML/doubleml-for-py/pull/86>`_ for details)
      - The joint Python and R docu and user guide is now served to
        `https://docs.doubleml.org <https://docs.doubleml.org>`_ from a separate repo
        `https://github.com/DoubleML/doubleml-docs <https://github.com/DoubleML/doubleml-docs>`_
      - Generate and upload a unit test coverage report to codecov
        `https://app.codecov.io/gh/DoubleML/doubleml-for-py <https://app.codecov.io/gh/DoubleML/doubleml-for-py>`_
        `#76 <https://github.com/DoubleML/doubleml-for-py/pull/76>`_
      - Run lint checks with flake8 `#78 <https://github.com/DoubleML/doubleml-for-py/pull/78>`_, align code with PEP8
        standards `#79 <https://github.com/DoubleML/doubleml-for-py/pull/79>`_, activate code quality checks at codacy
        `#80 <https://github.com/DoubleML/doubleml-for-py/pull/80>`_
      - Refactoring (reduce code redundancy) of the code for tuning of the ML learners used for approximation the
        nuisance functions `#81 <https://github.com/DoubleML/doubleml-for-py/pull/81>`_
      - Minor updates, bug fixes and improvements of the exception handling
        (contained in `#82 <https://github.com/DoubleML/doubleml-for-py/pull/82>`_ &
        `#89 <https://github.com/DoubleML/doubleml-for-py/pull/89>`_)

    .. dropdown:: DoubleML 0.1.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - Fixed a compatibility issue with ``scikit-learn`` 0.24, which only affected some unit tests
        (`#70 <https://github.com/DoubleML/doubleml-for-py/issues/70>`_, `#71 <https://github.com/DoubleML/doubleml-for-py/pull/71>`_)
      - Added scheduled unit tests on github-action (three times a week) `#69 <https://github.com/DoubleML/doubleml-for-py/pull/69>`_
      - Split up estimation of nuisance functions and computation of score function components. Further introduced a
        private method ``_est_causal_pars_and_se()``, see `#72 <https://github.com/DoubleML/doubleml-for-py/pull/72>`_.
        This is needed for the DoubleML-Serverless project: https://github.com/DoubleML/doubleml-serverless.

    .. dropdown:: DoubleML 0.1.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Bug fix in the drawing of bootstrap weights for the multiple treatment case
        `#66 <https://github.com/DoubleML/doubleml-for-py/pull/66>`_ (see also https://github.com/DoubleML/doubleml-for-r/pull/28)
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

    .. dropdown:: DoubleML 1.0.1
      :class-title: sd-bg-primary sd-font-weight-bold
      :open:

      - Maintenance (upcoming breaking changes from ``paradox`` package), thanks to new contributor Martin Binder `@mb706 <https://github.com/mb706>`_
        `# 195 <https://github.com/DoubleML/doubleml-for-r/pull/195>`_
        `# 198 <https://github.com/DoubleML/doubleml-for-r/pull/199>`_

    .. dropdown:: DoubleML 1.0.0
      :class-title: sd-bg-primary sd-font-weight-bold
      :open:

      - Update citation info to publication in Journal of Statistical Software, rename helper function and fix links and GH actions
        `191 <https://github.com/DoubleML/doubleml-for-r/pull/191>`_

    .. dropdown:: DoubleML 0.5.3
      :class-title: sd-bg-primary sd-font-weight-bold
      - Add documentation for estimated models for nuisance parameters
        `#181 <https://github.com/DoubleML/doubleml-for-r/pull/181>`_
      - New contributor `@SvenKlaassen <https://github.com/SvenKlaassen>`_
      - Maintenance
        `#179 <https://github.com/DoubleML/doubleml-for-r/pull/179>`_

    .. dropdown:: DoubleML 0.5.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - Store estimated models for nuisance parameters
        `#169 <https://github.com/DoubleML/doubleml-for-r/pull/169>`_
      - New maintainer of the CRAN package DoubleML `@PhilippBach <https://github.com/PhilippBach>`_
      - Maintenance
        `#170 <https://github.com/DoubleML/doubleml-for-r/pull/170>`_
        `#173 <https://github.com/DoubleML/doubleml-for-r/pull/173>`_
        `#174 <https://github.com/DoubleML/doubleml-for-r/pull/174>`_
        `#177 <https://github.com/DoubleML/doubleml-for-r/pull/177>`_
        `#178 <https://github.com/DoubleML/doubleml-for-r/pull/178>`_

    .. dropdown:: DoubleML 0.5.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Fix a CRAN issue (html checks) by regenerating ``.Rd``-files with the newest version of ``roxygen2``.
        `#166 <https://github.com/DoubleML/doubleml-for-r/issues/166>`_
        `#167 <https://github.com/DoubleML/doubleml-for-r/pull/167>`_
        `#168 <https://github.com/DoubleML/doubleml-for-r/pull/168>`_

    .. dropdown:: DoubleML 0.5.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Implement a new score function ``score = 'IV-type'`` for the PLIV model (for details see
        `#161 <https://github.com/DoubleML/doubleml-for-r/pull/161>`_) |br|
        --> **API change** from ``DoubleMLPLIV$new(obj_dml_data, ml_g, ml_m, ml_r [, ...])``
        to ``DoubleMLPLIV$new(obj_dml_data, ml_g, ml_m, ml_r, ml_g [, ...])``
      - Adapt the nuisance estimation for the ``'IV-type'`` score for the PLR model (for details see
        `#161 <https://github.com/DoubleML/doubleml-for-r/pull/161>`_) |br|
        --> **API change** from ``DoubleMLPLR$new(obj_dml_data, ml_g, ml_m [, ...])``
        to ``DoubleMLPLR$new(obj_dml_data, ml_l, ml_m, ml_g [, ...])``
      - Use ``task_type`` instead of ``learner_class`` to identify whether a learner is meant to regress or classify (this
        change makes it possible to easily integrate pipelines from ``mlr3pipelines`` as learner for the nuisance functions)
        `#141 <https://github.com/DoubleML/doubleml-for-r/pull/141>`_
      - Add `Contribution Guidelines <https://github.com/DoubleML/doubleml-for-r/blob/main/CONTRIBUTING.md>`_,
        issue templates, a pull request template and a
        `discussion forum <https://github.com/DoubleML/doubleml-for-r/discussions>`_ to the R package repository
        `#142 <https://github.com/DoubleML/doubleml-for-r/pull/142>`_
        `#146 <https://github.com/DoubleML/doubleml-for-r/pull/146>`_
        `#147 <https://github.com/DoubleML/doubleml-for-r/pull/147>`_
      - Allow the usage of classifiers for binary outcome variables in the model classes IRM and IIVM
        `#114 <https://github.com/DoubleML/doubleml-for-r/pull/114>`_
      - Bug fixes and maintenance
        `#155 <https://github.com/DoubleML/doubleml-for-r/issues/155>`_
        `#156 <https://github.com/DoubleML/doubleml-for-r/issues/156>`_
        `#157 <https://github.com/DoubleML/doubleml-for-r/issues/157>`_
        `#158 <https://github.com/DoubleML/doubleml-for-r/issues/158>`_
        `#160 <https://github.com/DoubleML/doubleml-for-r/pull/160>`_
        `#163 <https://github.com/DoubleML/doubleml-for-r/pull/163>`_

    .. dropdown:: DoubleML 0.4.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Prevent usage of ``glmnet`` learner for unit testing as recommended by CRAN (failing tests on Solaris)
        `#137 <https://github.com/DoubleML/doubleml-for-r/pull/137>`_
      - Prepare for the upcoming release of ``checkmate`` which is not backward compatible with our unit tests
        `#134 <https://github.com/DoubleML/doubleml-for-r/pull/134>`_

    .. dropdown:: DoubleML 0.4.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - **Release highlight:** Clustered standard errors for double machine learning models
        `#119 <https://github.com/DoubleML/doubleml-for-r/pull/119>`_
      - Apply styler as described in the wiki (https://github.com/DoubleML/doubleml-for-r/wiki/Style-Guidelines) and add a
        corresponding CI on github actions `#120 <https://github.com/DoubleML/doubleml-for-r/pull/120>`_
        `#122 <https://github.com/DoubleML/doubleml-for-r/pull/122>`_
      - Other refactoring, bug fixes and documentation updates
        `#127 <https://github.com/DoubleML/doubleml-for-r/pull/127>`_
        `#129 <https://github.com/DoubleML/doubleml-for-r/pull/129>`_
        `#130 <https://github.com/DoubleML/doubleml-for-r/pull/130>`_
        `#131 <https://github.com/DoubleML/doubleml-for-r/pull/131>`_
        `#132 <https://github.com/DoubleML/doubleml-for-r/pull/132>`_
        `#133 <https://github.com/DoubleML/doubleml-for-r/pull/133>`_

    .. dropdown:: DoubleML 0.3.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Initialize all numeric matrices, vectors and arrays with the correct data type by using ``NA_real_`` instead of
        ``NA`` and replace a ``print()`` call with ``cat()`` `#115 <https://github.com/DoubleML/doubleml-for-r/pull/115>`_

    .. dropdown:: DoubleML 0.3.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - Use active bindings in the R6 OOP implementation
        `#106 <https://github.com/DoubleML/doubleml-for-r/pull/106>`_ &
        `#93 <https://github.com/DoubleML/doubleml-for-r/issues/93>`_
      - Fix the aggregation formula for standard errors from repeated cross-fitting
        `#94 <https://github.com/DoubleML/doubleml-for-r/issues/94>`_ &
        `#95 <https://github.com/DoubleML/doubleml-for-r/pull/95>`_
      - Always use the same bootstrap algorithm independent of ``dml1`` vs ``dml2`` and consistent with docu and paper
        `#98 <https://github.com/DoubleML/doubleml-for-r/issues/98>`_ &
        `#99 <https://github.com/DoubleML/doubleml-for-r/pull/99>`_
      - Initialize predictions with NA and make sure that there are no misleading entries in the evaluated score
        functions `#96 <https://github.com/DoubleML/doubleml-for-r/issues/96>`_ &
        `#105 <https://github.com/DoubleML/doubleml-for-r/pull/105>`_
      - Avoid overriding learner parameters during tuning
        `#83 <https://github.com/DoubleML/doubleml-for-r/issues/83>`_ &
        `#84 <https://github.com/DoubleML/doubleml-for-r/pull/84>`_
      - Fixes in the exception handling and extension of the unit tests for the score function choice
        `#82 <https://github.com/DoubleML/doubleml-for-r/pull/82>`_
      - Prevent overwriting parameters from initialization when calling set_ml_nuisance_params
        `#87 <https://github.com/DoubleML/doubleml-for-r/issues/87>`_ &
        `#89 <https://github.com/DoubleML/doubleml-for-r/pull/89>`_
      - Major refactoring and cleanup and extension of the unit test framework
        `#101 <https://github.com/DoubleML/doubleml-for-r/pull/101>`_
      - Extension and reorganization of exception handling for ``DoubleMLData`` objects
        `#63 <https://github.com/DoubleML/doubleml-for-r/issues/63>`_ &
        `#90 <https://github.com/DoubleML/doubleml-for-r/pull/90>`_
      - Introduce style guide and clean up code
        `#80 <https://github.com/DoubleML/doubleml-for-r/pull/80>`_ &
        `#81 <https://github.com/DoubleML/doubleml-for-r/pull/81>`_
      - Adaption to be compatible with an API change in the next ``mlr3`` release
        `#103 <https://github.com/DoubleML/doubleml-for-r/pull/103>`_
      - Run unit tests with mlr3 in dev version on github actions
        `#104 <https://github.com/DoubleML/doubleml-for-r/pull/104>`_
      - Updated the citation info
        `#78 <https://github.com/DoubleML/doubleml-for-r/pull/78>`_,
        `#79 <https://github.com/DoubleML/doubleml-for-r/pull/79>`_ &
        `#86 <https://github.com/DoubleML/doubleml-for-r/pull/86>`_
      - Added a short version of and a reference to the arXiv paper as vignette
        `#110 <https://github.com/DoubleML/doubleml-for-r/pull/110>`_ &
        `#113 <https://github.com/DoubleML/doubleml-for-r/issues/113>`_
      - Prevent using the subclassed methods check_score and check_data when constructing DoubleML objects
        `#107 <https://github.com/DoubleML/doubleml-for-r/pull/107>`_
      - Other refactoring and minor adaptions
        `#91 <https://github.com/DoubleML/doubleml-for-r/pull/91>`_,
        `#92 <https://github.com/DoubleML/doubleml-for-r/pull/92>`_,
        `#102 <https://github.com/DoubleML/doubleml-for-r/pull/102>`_ &
        `#108 <https://github.com/DoubleML/doubleml-for-r/pull/108>`_

    .. dropdown:: DoubleML 0.2.1
      :class-title: sd-bg-primary sd-font-weight-bold

      - Provide an option to store & export the first-stage predictions
        `#74 <https://github.com/DoubleML/doubleml-for-r/pull/74>`_
      - Reduce and refine messaging to the console during estimation
        `#72 <https://github.com/DoubleML/doubleml-for-r/pull/72>`_
      - Fix bug in IIVM model if the IV variable is not named ``z``
        `#75 <https://github.com/DoubleML/doubleml-for-r/pull/75>`_
      - Fix failing unit test `#71 <https://github.com/DoubleML/doubleml-for-r/pull/71>`_
      - Added the package logo to the doc

    .. dropdown:: DoubleML 0.2.0
      :class-title: sd-bg-primary sd-font-weight-bold

      - In the PLR one can now also specify classifiers for ``ml_m`` in case of a binary treatment variable with values 0 and 1
      - Major refactoring of core-parts of the estimation and tuning of the ML estimators for the nuisance functions: All models now use central helper functions ``dml_cv_predict()`` and ``dml_tune()``
      - Extensions to the unit test framework to improve upon test coverage
      - Added unit test coverage via codecov: `https://app.codecov.io/gh/DoubleML/doubleml-for-r <https://app.codecov.io/gh/DoubleML/doubleml-for-r>`_
      - Minor docu updates and adaptions: `#58 <https://github.com/DoubleML/doubleml-for-r/pull/58>`_, `#61 <https://github.com/DoubleML/doubleml-for-r/pull/61>`_ & `#70 <https://github.com/DoubleML/doubleml-for-r/pull/70>`_

    .. dropdown:: DoubleML 0.1.2
      :class-title: sd-bg-primary sd-font-weight-bold

      - Adapt calls to ``mlr3tuning`` due to a change in their API (since version 0.6.0): fixes `#51 <https://github.com/DoubleML/doubleml-for-r/issues/51>`_
      - Add ``bbotk`` to suggests: fixes R CMD check note `#47 <https://github.com/DoubleML/doubleml-for-r/issues/47>`_
      - Use ``doi{}`` command: fixes R CMD check note `#54 <https://github.com/DoubleML/doubleml-for-r/issues/54>`_
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
