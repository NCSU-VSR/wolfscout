$(document).ready(function() {

    //////////////////////////////////////////////////////////////////////////////
    /**
     * INTERACTION DATA PAGE
     */

    /**
     * Sets the selected interaction group pk to id_interaction_to_be_exported hidden field.
     * This field is then grabbed by the export form in the apps.study.views to export that
     * clicked interaction data
     */
    $('.export_interaction_group_button').click(function() {
        // GET INTERACTION GROUP ID
        $('#id_interaction_to_be_exported').val($(this).attr("name"));
    });
    //////////////////////////////////////////////////////////////////////////////

    //////////////////////////////////////////////////////////////////////////////
    /**
     * ANIMAL EXPORT PAGE
      */

    $('.animalCheckbox').change(function() {
        checkAnimalSelected();
    });
    $('.sexCheckbox').change(function() {
        checkAnimalSelected();
    });
    $('.speciesCheckbox').change(function() {
        checkAnimalSelected();
    });
    $('.ageCheckbox').change(function() {
        checkAnimalSelected();
    });

    var isAnimalDisabled = false;
    var isEverythingElseDisabled = false;

    //Initially sets the Export Animal CSV button to disabled
    blockEnabledDisable_Field_Animal('.export_animal_csv', false, 'button');

    /**
     * Checks to see if an animal is selected from the list of animals.  If so, enables the
     * export animal csv button. If not, disables it
     */
    function checkAnimalSelected(){
        var isAnimalSelected = $('.animalCheckbox').parents('table').find(':checkbox').is(':checked');
        var isSexSelected = $('.sexCheckbox').parents('table').find(':checkbox').is(':checked');
        var isSpeciesSelected = $('.speciesCheckbox').parents('table').find(':checkbox').is(':checked');
        var isAgeSelected = $('.ageCheckbox').parents('table').find(':checkbox').is(':checked');

        if(isAnimalSelected){ //&& !isEverythingElseDisabled){
            blockEnabledDisable_Field_Animal('.age_header', false, 'li');
            blockEnabledDisable_Field_Animal('.species_header', false, 'li');
            blockEnabledDisable_Field_Animal('.sex_header', false, 'li');
            isEverythingElseDisabled = true;

            blockEnabledDisable_Field_Animal('.export_animal_csv', true, 'button');
        }else{
            blockEnabledDisable_Field_Animal('.age_header', true, 'li');
            blockEnabledDisable_Field_Animal('.species_header', true, 'li');
            blockEnabledDisable_Field_Animal('.sex_header', true, 'li');
            if(isSexSelected || isSpeciesSelected || isAgeSelected){
                if(!isAnimalDisabled){
                    blockEnabledDisable_Field_Animal('.animal_header', false, 'li');
                }
                isAnimalDisabled = true;
            }else{
                blockEnabledDisable_Field_Animal('.animal_header', true, 'li');
                isAnimalDisabled = false;
            }
            isEverythingElseDisabled = false;

            blockEnabledDisable_Field_Animal('.export_animal_csv', false, 'button');
        }
    }

    //Sets the export type to CSV if CSV is clicked
    $('.export_animal_csv').click(function() {
        $('#id_is_csv').attr('checked','checked');
        $('#id_is_shape').removeAttr('checked');
    });

    //Sets the export type to SHAPE if SHAPE is clicked
    $('.export_animal_shape').click(function() {
        $('#id_is_csv').removeAttr('checked');
        $('#id_is_shape').attr('checked','checked');
    });

    //If Collar Filter checkbox clicked - set status of export buttons
    $('.enableExport_collarFilter_ANIMAL_EXPORT_PAGE').change(function() {
        checkCollarAndFilterOptionsSelected_ANIMAL_EXPORT_PAGE();
    });
    //If Weather Filter checkbox clicked - set status of export buttons
    $('.enableExport_weatherFilter_ANIMAL_EXPORT_PAGE').change(function() {
        checkCollarAndFilterOptionsSelected_ANIMAL_EXPORT_PAGE();
    });

    /**
     * If there are no COllar or Weather filter options selected, disable export buttons
     * Special case: if LOCATION is not selected under collar filter options, disable shape export
     * considering LOCATION information is the minimum requirements of a shape
     */
    function checkCollarAndFilterOptionsSelected_ANIMAL_EXPORT_PAGE(){
        var isCollarFilterSelected = $('.enableExport_collarFilter_ANIMAL_EXPORT_PAGE').parents('table').find(':checkbox').is(':checked');
        var isWeatherFilterSelected = $('.enableExport_weatherFilter_ANIMAL_EXPORT_PAGE').parents('table').find(':checkbox').is(':checked');

        if(isCollarFilterSelected || isWeatherFilterSelected){
            blockEnabledDisable_Field_Collar('.export_animal_csv', true, "button");
            /*if($('#id_collar_filter_LOCATION').is(':checked')){
                blockEnabledDisable_Field_Collar('.export_animal_shape', true, "button");
            }else{
                blockEnabledDisable_Field_Collar('.export_animal_shape', false, "button");
            }*/
        }else{
            blockEnabledDisable_Field_Collar('.export_animal_csv', false, "button");
            //blockEnabledDisable_Field_Collar('.export_animal_shape', false, "button");
        }
    }

    /**
     * Sets the field's parent's block status, essentially enabling/disabling
     * @param field
     * @param enable
     * @param parent
     */
    function blockEnabledDisable_Field_Animal(field, enable, parent){
        field = $(field).parent(parent);
        if(enable){
            field.attr('disabled', false);
            field.unblock();
        }else{
            if(!enable){
                field.attr('disabled', true);
                field.block({
                    message: '',
                    css: {
                        border: 'none',
                        padding: '15px',
                        backgroundColor: '#000',
                        '-webkit-border-radius': '10px',
                        '-moz-border-radius': '10px',
                        opacity: .6,
                        color: '#fff',
                        cursor: null
                    },

                    // styles for the overlay
                    overlayCSS:  {
                        backgroundColor: '#000',
                        opacity:         0.4,
                        '-webkit-border-radius': '10px',
                        '-moz-border-radius':    '10px'
                    }
                });
            }
        }
    }
    //////////////////////////////////////////////////////////////////////////////

    //////////////////////////////////////////////////////////////////////////////
    /**
     * COLLAR EXPORT PAGE
     */

    // Initially disable export buttons
    blockEnabledDisable_Field_Collar('.export_multi_collardata_csv', false, "button");
    blockEnabledDisable_Field_Collar('.export_multi_collardata_shape', false, "button");

    //If export multi csv clicked, set as export type
    $('.export_multi_collardata_csv').click(function() {
        $('#id_is_multi_shape').removeAttr('checked');
        $('#id_is_single_csv').removeAttr('checked');
        $('#id_is_single_shape').removeAttr('checked');
        $('#id_is_multi_csv').attr('checked','checked');
    });
    //If export multi shape clicked, set as export type
    $('.export_multi_collardata_shape').click(function() {
        $('#id_is_multi_csv').removeAttr('checked');
        $('#id_is_single_csv').removeAttr('checked');
        $('#id_is_single_shape').removeAttr('checked');
        $('#id_is_multi_shape').attr('checked','checked');
    });
    //If export single csv clicked, set as export type
    $('.is_single_csv').click(function() {
        $('#id_is_multi_csv').removeAttr('checked');
        $('#id_is_multi_shape').removeAttr('checked');
        $('#id_is_single_shape').removeAttr('checked');
        $('#id_is_single_csv').attr('checked','checked');
        // GET COLLAR ID
        $('#id_single_export').val($(this).attr("name"));
    });
    //If export single shape clicked, set as export type
    $('.is_single_shape').click(function() {
        $('#id_is_multi_csv').removeAttr('checked');
        $('#id_is_multi_shape').removeAttr('checked');
        $('#id_is_single_csv').removeAttr('checked');
        $('#id_is_single_shape').attr('checked','checked');
        // GET COLLAR ID
        $('#id_single_export').val($(this).attr("name"));
    });

    // If any collar checkbox state change - perform relevant UI logic
    $('.enableExport').change(function() {
        checkCollarAndFilterOptionsSelected_COLLAR_EXPORT_PAGE();
    });
    // If any collar FILTER checkbox state change - perform relevant UI logic
    $('.enableExport_collarFilter_COLLAR_EXPORT_PAGE').change(function() {
        checkCollarAndFilterOptionsSelected_COLLAR_EXPORT_PAGE();
    });
    // If any weather FILTER checkbox state change - perform relevant UI logic
    $('.enableExport_weatherFilter_COLLAR_EXPORT_PAGE').change(function() {
        checkCollarAndFilterOptionsSelected_COLLAR_EXPORT_PAGE();
    });

    /**
     * If there are no COllar or Weather filter options selected, disable export buttons
     * Special case: if LOCATION is not selected under collar filter options, disable shape export
     * considering LOCATION information is the minimum requirements of a shape
     */
    function checkCollarAndFilterOptionsSelected_COLLAR_EXPORT_PAGE(){
        var isCollarSelected = $('.enableExport').parents('table').find(':checkbox').is(':checked');
        var isCollarFilterSelected = $('.enableExport_collarFilter_COLLAR_EXPORT_PAGE').parents('table').find(':checkbox').is(':checked');
        var isWeatherFilterSelected = $('.enableExport_weatherFilter_COLLAR_EXPORT_PAGE').parents('table').find(':checkbox').is(':checked');

        if(isCollarSelected){
            if(isCollarFilterSelected || isWeatherFilterSelected){
                blockEnabledDisable_Field_Collar('.export_multi_collardata_csv', true, "button");
                blockEnabledDisable_Field_Collar('.export_single_collardata_csv', true, "button");
                if($('#id_collar_filter_LOCATION').is(':checked')){
                    blockEnabledDisable_Field_Collar('.export_multi_collardata_shape', true, "button");
                    blockEnabledDisable_Field_Collar('.export_single_collardata_shape', true, "button");
                }else{
                    blockEnabledDisable_Field_Collar('.export_multi_collardata_shape', false, "button");
                    blockEnabledDisable_Field_Collar('.export_single_collardata_shape', false, "button");
                }
            }else{
                blockEnabledDisable_Field_Collar('.export_multi_collardata_csv', false, "button");
                blockEnabledDisable_Field_Collar('.export_multi_collardata_shape', false, "button");
                blockEnabledDisable_Field_Collar('.export_single_collardata_csv', false, "button");
                blockEnabledDisable_Field_Collar('.export_single_collardata_shape', false, "button");
            }
        }else{
            if(isCollarFilterSelected || isWeatherFilterSelected){
                blockEnabledDisable_Field_Collar('.export_single_collardata_csv', true, "button");
                if($('#id_collar_filter_LOCATION').is(':checked')){
                    blockEnabledDisable_Field_Collar('.export_single_collardata_shape', true, "button");
                }else{
                    blockEnabledDisable_Field_Collar('.export_single_collardata_shape', false, "button");
                }
            }else{
                blockEnabledDisable_Field_Collar('.export_single_collardata_csv', false, "button");
                blockEnabledDisable_Field_Collar('.export_single_collardata_shape', false, "button");
            }
            blockEnabledDisable_Field_Collar('.export_multi_collardata_csv', false, "button");
            blockEnabledDisable_Field_Collar('.export_multi_collardata_shape', false, "button");
        }
    }
    /**
     * Sets the field's parent's block status, essentially enabling/disabling.  The difference here between this
     * blockEnabled method and the one above is this one checks if the parent field was previously disabled, removing
     * the possibility of multiple blocking over and over again, which is taxing on the DOM
     * @param field
     * @param enable
     * @param parent
     */
    function blockEnabledDisable_Field_Collar(field, enable, parent){
        field = $(field).parent(parent);
        if(enable && field.is(':disabled')){
            field.attr('disabled', false);
            field.unblock();
        }else{
            if(!enable && !field.is(':disabled')){
                field.attr('disabled', true);
                field.block({
                    message: '',
                    css: {
                        border: 'none',
                        padding: '15px',
                        backgroundColor: '#000',
                        '-webkit-border-radius': '10px',
                        '-moz-border-radius': '10px',
                        opacity: .6,
                        color: '#fff',
                        cursor: null
                    },

                    // styles for the overlay
                    overlayCSS:  {
                        backgroundColor: '#000',
                        opacity:         0.4,
                        '-webkit-border-radius': '10px',
                        '-moz-border-radius':    '10px'
                    }
                });
            }
        }
    }
    // HIDE EXPORT TYPE FIELDS
    $('.export_box_hidden').hide();
});