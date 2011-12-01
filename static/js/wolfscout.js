$(document).ready(function() {
    //////////////////////////////////////////////////////////////////////////////
    /**
     * INTERACTION DATA PAGE
     */
    $('.enableDistance').change(function() {
        if($(this).parents('table').find(':checkbox').is(':checked')){
            blockEnabledDisable_Field_Specimen('#id_distance_in_km', true, "p");
            blockEnabledDisable_Field_Specimen('#id_selected_collars', true, "p");
        }else{
            blockEnabledDisable_Field_Specimen('#id_distance_in_km', false, "p");
            blockEnabledDisable_Field_Specimen('#id_selected_collars', false, "p");
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

    blockEnabledDisable_Field_Specimen('#id_distance_in_km', false, "p");
    blockEnabledDisable_Field_Specimen('#id_selected_collars', false, "p");
    //////////////////////////////////////////////////////////////////////////////

    //////////////////////////////////////////////////////////////////////////////
    /**
     * SPECIMEN EXPORT PAGE
      */
    $('.specimenCheckbox').change(function() {
        checkSpecimenSelected();
    });

    function checkSpecimenSelected(){
        var isSpecimenSelected = $('.specimenCheckbox').parents('table').find(':checkbox').is(':checked');

        if(isSpecimenSelected){
            blockEnabledDisable_Field_Specimen('.species_tab', false, 'div');
            blockEnabledDisable_Field_Specimen('.sex_tab', false, 'div');
        }else{
            blockEnabledDisable_Field_Specimen('.species_tab', true, 'div');
            blockEnabledDisable_Field_Specimen('.sex_tab', true, 'div');
        }
    }

    function blockEnabledDisable_Field_Specimen(field, enable, parent){
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

    blockEnabledDisable_Field_Collar('.export_collardata', false, "button");

    $('.export_collardata').click(function() {
        $('#id_is_multi').attr('checked','checked');
    });

    $('.is_single').click(function() {
        $('#id_is_multi').removeAttr('checked');
        $('#id_single_export').val($(this).attr("name"));
    });

    //INTERACTION PAGE CHECKBOX FUNCTIONS
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
                blockEnabledDisable_Field_Collar('.export_collardata', true, "button");
                blockEnabledDisable_Field_Collar('.export_single_collardata', true, "button");
            }else{
                blockEnabledDisable_Field_Collar('.export_collardata', false, "button");
                blockEnabledDisable_Field_Collar('.export_single_collardata', false, "button");
            }
        }else{
            if(isCollarFilterSelected || isWeatherFilterSelected){
                blockEnabledDisable_Field_Collar('.export_single_collardata', true, "button");
            }else{
                blockEnabledDisable_Field_Collar('.export_single_collardata', false, "button");
            }
            blockEnabledDisable_Field_Collar('.export_collardata', false, "button");
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