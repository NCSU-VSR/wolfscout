$(document).ready(function() {
    //////////////////////////////////////////////////////////////////////////////
    /**
     * INTERACTION DATA PAGE
     */
    $('.enableDistance').change(function() {
        if($(this).parents('table').find(':checkbox').is(':checked')){
            blockEnabledDisable_Field_Animal('#id_distance_in_km', true, "p");
            blockEnabledDisable_Field_Animal('#id_selected_collars', true, "p");
        }else{
            blockEnabledDisable_Field_Animal('#id_distance_in_km', false, "p");
            blockEnabledDisable_Field_Animal('#id_selected_collars', false, "p");
        }
        //Update collar list
        var collarList = '';
        $('.enableDistance').each(function(){
            if($(this).is(':checked')){
                collarList += $(this).closest("td").next().html() + ', ';
            }
        });
       $('#id_selected_collars').val($.trim(collarList).slice(0, -1));
    });

    blockEnabledDisable_Field_Animal('#id_distance_in_km', false, "p");
    blockEnabledDisable_Field_Animal('#id_selected_collars', false, "p");
    //////////////////////////////////////////////////////////////////////////////

    //////////////////////////////////////////////////////////////////////////////
    /**
     * ANIMAL EXPORT PAGE
      */
    /*$('.animalCheckbox').change(function() {
        checkAnimalSelected();
    });

    function checkAnimalSelected(){
        var isAnimalSelected = $('.animalCheckbox').parents('table').find(':checkbox').is(':checked');

        if(isAnimalSelected){
            blockEnabledDisable_Field_Animal('.species_tab', false, 'div');
            blockEnabledDisable_Field_Animal('.sex_tab', false, 'div');
        }else{
            blockEnabledDisable_Field_Animal('.species_tab', true, 'div');
            blockEnabledDisable_Field_Animal('.sex_tab', true, 'div');
        }
    }*/

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
                        opacity:         0.2,
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
    // HIDE EXPORT TYPE FIELDS
    $('.export_box_hidden').hide();

    blockEnabledDisable_Field_Collar('.export_multi_collardata_csv', false, "button");

    blockEnabledDisable_Field_Collar('.export_multi_collardata_shape', false, "button");

    $('.export_multi_collardata_csv').click(function() {
        $('#id_is_multi_shape').removeAttr('checked');
        $('#id_is_single_csv').removeAttr('checked');
        $('#id_is_single_shape').removeAttr('checked');
        $('#id_is_multi_csv').attr('checked','checked');
    });

    $('.export_multi_collardata_shape').click(function() {
        $('#id_is_multi_csv').removeAttr('checked');
        $('#id_is_single_csv').removeAttr('checked');
        $('#id_is_single_shape').removeAttr('checked');
        $('#id_is_multi_shape').attr('checked','checked');
    });

    $('.is_single_csv').click(function() {
        $('#id_is_multi_csv').removeAttr('checked');
        $('#id_is_multi_shape').removeAttr('checked');
        $('#id_is_single_shape').removeAttr('checked');
        $('#id_is_single_csv').attr('checked','checked');
        // GET COLLAR ID
        $('#id_single_export').val($(this).attr("name"));
    });

    $('.is_single_shape').click(function() {
        $('#id_is_multi_csv').removeAttr('checked');
        $('#id_is_multi_shape').removeAttr('checked');
        $('#id_is_single_csv').removeAttr('checked');
        $('#id_is_single_shape').attr('checked','checked');
        // GET COLLAR ID
        $('#id_single_export').val($(this).attr("name"));
    });

    // If any checkbox checkbox state change - perform relevant UI logic
    $('.enableExport').change(function() {
        checkCollarAndFilterOptionsSelected();
    });

    $('.enableExport_collarFilter').change(function() {
        checkCollarAndFilterOptionsSelected();
    });

    $('.enableExport_weatherFilter').change(function() {
        checkCollarAndFilterOptionsSelected();
    });

    function checkCollarAndFilterOptionsSelected(){
        var isCollarSelected = $('.enableExport').parents('table').find(':checkbox').is(':checked');
        var isCollarFilterSelected = $('.enableExport_collarFilter').parents('table').find(':checkbox').is(':checked');
        var isWeatherFilterSelected = $('.enableExport_weatherFilter').parents('table').find(':checkbox').is(':checked');

        if(isCollarSelected){
            if(isCollarFilterSelected || isWeatherFilterSelected){
                blockEnabledDisable_Field_Collar('.export_multi_collardata_csv', true, "button");
                blockEnabledDisable_Field_Collar('.export_single_collardata_csv', true, "button");
                if($('#id_LOCATION').is(':checked')){
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
                if($('#id_LOCATION').is(':checked')){
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
});