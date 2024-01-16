// Adicione este script para manipular o envio do formulário e exibir os alertas
$(document).ready(function () {
  $("#agendamentoForm").submit(function (event) {
    event.preventDefault();

    $.ajax({
      type: "POST",
      url: $(this).attr("action"),
      data: $(this).serialize(),
      success: function (response) {
        if (response.status === "success") {
          alert(
            "Agendamento feito com sucesso! Agendamento ID: " +
              response.agendamento_id
          );
        } else {
          alert(
            "Erro ao agendar. Verifique os dados e tente novamente.\n" +
              response.message
          );
        }
      },
      error: function () {
        alert("Erro ao processar a solicitação. Tente novamente mais tarde.");
      },
    });
  });
});
