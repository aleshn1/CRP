var SPMaskBehavior = function (val) {
  return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
  onKeyPress: function(val, e, field, options) {
      field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};


django.jQuery(document).ready(function() {
    django.jQuery('.dt_nascimento').mask('00/00/0000');
    django.jQuery('.cpf').mask('000.000.000-00', {reverse: true});
    django.jQuery('.telefone').mask('(00) 0000-0000');
    django.jQuery('.celular').mask(SPMaskBehavior, spOptions);
    django.jQuery('.dt_promessa').mask('00/00/0000');
    django.jQuery('.dt_matrimonio').mask('00/00/0000');
    django.jQuery('.dt_entrada').mask('00/00/0000');
    django.jQuery('.cep').mask('00.000-000');
});

django.jQuery(document).ready(function() {
    function toggleAtestadoObitoField() {
        var falecidoSelecionado = django.jQuery(".falecido").val();

        if (falecidoSelecionado === "true") {
            django.jQuery(".form-row.field-atestado_obito").show();
            console.log("aberto");
        } else {
            django.jQuery(".form-row.field-atestado_obito").hide();
            console.log("fechado");
        }
    }

    // Chame a função inicialmente para lidar com o estado inicial
    toggleAtestadoObitoField();

    // Vincule a função ao evento de alteração do campo "falecido"
    django.jQuery(".falecido").change(function() {
        toggleAtestadoObitoField();
    });
});




